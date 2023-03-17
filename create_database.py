import psycopg2
from psycopg2 import sql
from contextlib import closing
from app.config import config

database_credentials = config()





with closing(psycopg2.connect(database_credentials)) as conn:
    cursor = conn.cursor()
    query = ''' IF NOT EXIST CREATE DATABASE {} ;'''
    name = 'mailchimp'

    conn.autocommit = True
    cursor.execute(sql.SQL(query).format(
        sql.Identifier(name)))


