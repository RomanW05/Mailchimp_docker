# This file is for running uvicorn
FROM python:3.11.2-bullseye

RUN pip install pipreqs

RUN mkdir -p home/app

RUN pip install -Iv celery==5.2.7
RUN pip install -Iv cryptography==35.0.0
RUN pip install -Iv fastapi==0.92.0
RUN pip install -Iv geocoder==1.38.1
RUN pip install -Iv geopy==2.2.0
RUN pip install -Iv httpagentparser==1.9.5
RUN pip install -IV jinja2
RUN pip install -Iv jsonschema==4.17.3
RUN pip install -Iv psycopg2==2.9.5
RUN pip install -Iv psycopg2_binary==2.9.3
RUN pip install -Iv pydantic==1.8.2
RUN pip install -Iv pytest==7.0.1
RUN pip install -Iv starlette==0.25.0
RUN pip install -Iv uvicorn==0.21.1
# RUN pip install uvicorn

COPY . /home/app

WORKDIR /home/app

RUN pipreqs

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--reload"]
