import uvicorn

import time
from os import getcwd

from apischema.schema import Generate_email_schema, Load_template_schema, New_user_schema, Subscriber_status, New_campaign_schema
from apischema.encoder import Encoder

from controller.extractors import strip_user_agent, json_parameters_extractor, location_extractor

from starlette.requests import Request
from starlette.responses import Response, RedirectResponse, JSONResponse
from starlette.routing import Route, Mount
from starlette.templating import Jinja2Templates

from persistence.credentials import Credentials_from_file, Credentials_from_input, Encoder_credentials_from_file
from persistence.mapper.memory import MysqlDatabase
from persistence.database_manager import Database_manager
from persistence.encode_manager import Encode_manager

from fastapi import FastAPI, status, HTTPException, File, UploadFile, WebSocket
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

# from tasks import email_to_send

# from usecases import queue_emails
app = FastAPI()

templates = Jinja2Templates(directory='templates/')
app.mount("/static", StaticFiles(directory="static"), name="static")

credentials = Credentials_from_file()
database = MysqlDatabase(credentials.params())
db = Database_manager(database=database)


encoder_key = Encoder_credentials_from_file()
personal_encoder = Encoder(credentials=encoder_key.params())
encoder = Encode_manager(encoder=personal_encoder)


def apply_header_options(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["HTTP-HEADER"] = "VALUE"



@app.get("/")
def home(request: Request) -> Response:
    response = templates.TemplateResponse('index.html', {'request': request})
    apply_header_options(response)
    return response


@app.get("/generate_email", response_model=Generate_email_schema, response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def generate_email(request: Request) -> Response:
    all_templates = db._load_all_templates()

    response = templates.TemplateResponse('generate_email.html', context={'request': request, 'templates': all_templates})
    apply_header_options(response)

    return response


@app.get("/load_template/{_id}", response_model=Load_template_schema, status_code=status.HTTP_200_OK, response_class=HTMLResponse)
def load_template(request: Request, _id:int) -> Response:
    all_templates = db._load_all_templates()
    _id, name, plain_data, html_data, design_data = db._load_single_template(_id)

    response = templates.TemplateResponse('generate_email.html', context={'request': request, 'templates': all_templates, '_id':_id, "name":name, "data":design_data})
    apply_header_options(response)

    return response




@app.post("/update_template", response_class=HTMLResponse, status_code=status.HTTP_202_ACCEPTED)
async def update_template(request: Request) -> Response:
    form_data = await request.form()
    results = jsonable_encoder(form_data)

    name = results['name']
    plain_data = results['plain_data']
    html_data = results['html_data']
    design_data = results['design_data']
    _id = int(results['internal_id'])

    result = db._update_template(name, _id, plain_data, html_data, design_data)
    if not result:
        raise HTTPException(status_code=404, detail=f"Template with id {_id} not found")
    
    _id, name, plain_data, html_data, design_data = db._load_single_template(_id)
    all_templates = db._load_all_templates()

    response = templates.TemplateResponse('generate_email.html', context={'request': request, 'templates': all_templates, '_id':_id, "name":name, "data":design_data})
    apply_header_options(response)

    return response



@app.post("/save_template", status_code=status.HTTP_201_CREATED, response_class=HTMLResponse)
async def save_template(request: Request) -> Response:
    form_data = await request.form()
    results = jsonable_encoder(form_data)
    name = results['name']
    plain_data = results['plain_data']
    html_data = results['html_data']
    design_data = results['design_data']

    results = db._save_template(name, plain_data, html_data, design_data)
    _id, name, plain_data, html_data, design_data = db._load_latest_template()
    all_templates = db._load_all_templates()

    response = templates.TemplateResponse('generate_email.html', context={'request': request, 'templates': all_templates, '_id':_id, "name":name, "data":design_data})
    apply_header_options(response)

    return response


@app.delete("/delete_template/{_id}", response_class=HTMLResponse, status_code=status.HTTP_204_NO_CONTENT)
def delete_template(_id: int) -> RedirectResponse:
    result = db._delete_template(_id)
    if not result:
        raise HTTPException(status_code=404, detail=f"Template with id {_id} not found")
    
    redirect_url = '/generate_email'
    return RedirectResponse(redirect_url, status_code=303)


@app.get("/add_subscriber", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def add_subscriber(request: Request) -> Response:
    response = templates.TemplateResponse('register.html', {'request': request})
    apply_header_options(response)
    return response


@app.post("/new_subscriber", status_code=status.HTTP_201_CREATED, response_class=HTMLResponse)
async def new_subscriber(request: Request) -> Response:
    form_data = await request.form()
    results = jsonable_encoder(form_data)
    db_response = db._create_user({'email': results['email'], 'name': results['name']})
    redirect_url = '/add_subscriber'

    return RedirectResponse(redirect_url, status_code=303)


@app.get("/unsubscribe_subscriber/{_hash}", status_code=status.HTTP_201_CREATED, response_class=HTMLResponse)
async def unsubscribe_subscriber(request: Request, _hash:str) -> Response:
    parameters = encoder.decode_to_json(_hash)
    result = db._unsubscribe_user(parameters['email'])
    status = 'unsubscribed'
    # Subscriber_status
    resubscribe_message = f'''You have been successfully unsubscribed from our mailing list.
        It is a petty to see you go, {parameters['name']}. Resubscribe again in case you misclicked
    '''
    resubscribe_link = f'/resubscribe_subscriber/{_hash}'
    
    response =  templates.TemplateResponse(
        'subscriber_status.html',
            {
                'request': request,
                'status': status,
                'resubscribe_message': resubscribe_message,
                'resubscribe_link': resubscribe_link
            }
    )
    apply_header_options(response)

    return response


@app.get("/resubscribe_subscriber/{_hash}", status_code=status.HTTP_201_CREATED, response_class=HTMLResponse)
async def unsubscribe_subscriber(request: Request, _hash:str) -> Response:
    parameters = encoder.decode_to_json(_hash)
    db._resubscribe_user(parameters['email'])

    return 'you have been successfully resubscribe to our mailing list'


@app.get("/create_campaign", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
def create_campaign(request: Request) -> Response:
    response =  templates.TemplateResponse('new_campaign.html', {'request': request})

    apply_header_options(response)

    return response
    

@app.post('/save_campaign', tags=['Form'], status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def save_campaign(request: Request) -> Response:
    form_data = await request.form()
    results = jsonable_encoder(form_data)

    _id = db._get_campaign_id(results['name'])
    if _id is None:
        db._create_new_campaign(results['name'])
    redirect_url = '/create_campaign'

    return RedirectResponse(redirect_url, status_code=303)


@app.get("/launch_campaign", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
def load_templates(request: Request) -> Response:
    all_templates = db._load_all_templates()

    response = templates.TemplateResponse('launch_campaign.html', {'request': request, 'templates': all_templates})
    apply_header_options(response)

    return response



@app.get("/launch_campaign/{template_id}", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
def launch_campaign(request: Request, template_id:int) -> Response:
    campaigns = db._get_all_campaigns()
    all_templates = db._load_all_templates()
    _id, template_name, plain_data, html_data, design_data = db._load_single_template(template_id)

    response =  templates.TemplateResponse('launch_campaign.html', {
        'request': request,
        'campaigns':campaigns,
        'templates': all_templates,
        'data': design_data,
        'template_id':template_id,
        'template_name':template_name}
    )
    apply_header_options(response)

    return response

    
@app.post('/send_emails', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def send_emails(request: Request) -> Response:
    form_data = await request.form()
    results = jsonable_encoder(form_data)

    response = templates.TemplateResponse('sending_email_status.html', {'request': request}, status_code=303)
    apply_header_options(response)

    return response

    # Create queue
    queue_emails(**results)

    return RedirectResponse('/stream_event', status_code=303)


@app.websocket('/stream_event')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    for x in range(1):
        data = x
        await websocket.send_text(f"Current works is: {data}")
        time.sleep(1)
    
    await websocket.send_text(f"All emails were sent")
    time.sleep(1)
    await websocket.close()

    return RedirectResponse('/', status_code=303)
    return 'all emails were sent'


async def queue_emails(**kwargs):
    print(kwargs)
    template_id = int(kwargs['template_id'])
    campaign_id = int(kwargs['campaign_id'])
    campaign_name = kwargs["campaign_name"]
    base_url = kwargs["url"]

    subscribers_list = db._get_subscribed_subscribers()
    for subscriber in subscribers_list:
        subscriber_id, subscriber_email, subscriber_name = subscriber
        parameters = {
            'name': subscriber_name,
            'email': subscriber_email,
            'subscriber_id': int(subscriber_id),
            'template_id': template_id,
            'campaign_id': campaign_id
        }
        encoded_params = encoder.encode(parameters)
        queue_params = {
            "campaign_id": campaign_id,
            "campaign_name": campaign_name,
            "template_id": template_id,
            "subscriber_id": subscriber_id,
            "subscriber_email": subscriber_email,
            "subscriber_name": subscriber_name,
            "encoded_params": encoded_params,
            "base_url": base_url
        }
        results = email_to_send.delay(**queue_params)
        # await websocket.send_text(f"All emails were sent")
        yield results
    
    for x in range(10):
        time.sleep(1)
        yield x




@app.get("/white_pixel/{encoded_parameters}", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def white_pixel(request: Request, encoded_parameters:str) -> Response:
    filename = '/static/images/1px.png'
    path = getcwd() + filename
    ip = request._headers['host']
    os, browser = strip_user_agent(request._headers['user-agent'])
    json_parameters = encoder.decode_to_json(encoded_parameters)
    subscriber_id, template_id, campaign_id = json_parameters_extractor(json_parameters)

    os_id = db._load_os_id(os)
    browser_id = db._load_browser_id(browser)
    city, country = location_extractor(ip)
    country_id = db._load_country_id(country)
    city_id = db._load_city_id({'city':city, 'country':country})

    data = {
        'fk_subscriber_id':subscriber_id,
        'fk_campaign_id':campaign_id,
        'section':0,
        'fk_os_id':os_id,
        'fk_browser_id':browser_id,
        'fk_country_id':country_id,
        'fk_city_id':city_id,
        'ip':ip
    }
    db._update_campaign(data)

    return FileResponse(path=path, media_type='application/octet-stream', filename=filename)


if __name__ == '__main__':
    print('api running')
    uvicorn.run(app, host="0.0.0.0", port=8000)


# @app.get("/view_stats/{campaign_id}")
# async def view_stats(request: Request, campaign_id:int) -> Response:
#     campaign = db._get_campaign(campaign_id)
#     campaign_name = campaign[1]
#     campaign_id = campaign[0]
#     subscribers = db._get_subscribers(campaign_id)
#     subscribers_count = len(subscribers)
#     opened = db._get_opened(campaign_id)
#     opened_count = len(opened)
#     clicked = db._get_clicked(campaign_id)
#     clicked_count = len(clicked)
#     unsubscribed = db._get_unsubscribed(campaign_id)
#     unsubscribed_count = len(unsubscribed)
#     bounced = db._get_bounced(campaign_id)
#     bounced_count = len(bounced)