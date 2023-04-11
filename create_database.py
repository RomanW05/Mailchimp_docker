import psycopg2
from psycopg2 import sql
from contextlib import closing
# from config import config

database_credentials = {
    'host': 'localhost',
    # 'database': 'mailchimp',
    'user': 'postgres',
    'password': 123,
    'port': 5432
}
# '''
# select exists(
#  SELECT datname FROM pg_catalog.pg_database WHERE lower(datname) = lower('mailchimp')
# );
# '''

# with closing(psycopg2.connect(database_credentials)) as conn:
#     cursor = conn.cursor()

#     # Check if database exists
#     cursor.execute('''SELECT EXISTS(
#         SELECT datname FROM pg_catalog.pg_database WHERE lower(datname) = lower('mailchimp')
#         );'''
#     )
#     result = cursor.fetchone()
#     if result == False:

#         query = ''' CREATE DATABASE {} ;'''
#         name = 'mailchimp'

#         # conn.autocommit = True
#         cursor.execute(sql.SQL(query).format(
#             sql.Identifier(name)
#             ))
#         conn.commit()


