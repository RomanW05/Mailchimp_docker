from celery import Celery

from persistence.credentials import Credentials_from_file, Credentials_from_input, Encoder_credentials_from_file
from persistence.mapper.memory import MysqlDatabase
from persistence.database_manager import Database_manager

from usecases import custom_email, send_single_email
from apischema.schema import Email_to_send_task

from config import email_credentials


credentials = Credentials_from_file()
database = MysqlDatabase(credentials.params())
db = Database_manager(database=database)

app = Celery('tasks', broker='pyamqp://guest@RabbitMQ//')




@app.task
def email_to_send(**kwargs: Email_to_send_task):
    queue_params = kwargs
    campaign_id = queue_params["campaign_id"]
    campaign_name = queue_params["campaign_name"]
    template_id = queue_params["template_id"]
    subscriber_id = queue_params["subscriber_id"]
    subscriber_email = queue_params["subscriber_email"]
    subscriber_name = queue_params["subscriber_name"]
    encoded_params = queue_params ["encoded_params"]
    base_url = queue_params["base_url"]

    results = db._load_single_template(template_id)
    _id = results[0]
    name = results[1]
    plain_template = results[2]
    html_template = results[3]
    design_template = results[4]
    html_email, plain_email = custom_email(encoded_params, subscriber_name, html_template, plain_template, base_url)
    result = send_single_email(html_email, plain_email, campaign_name, subscriber_email, email_credentials())

