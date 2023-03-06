import psycopg2
from config import config
from contextlib import closing

# connection establishment
with closing(psycopg2.connect(config())) as conn:

    conn.autocommit = True
    
    # Creating a cursor object
    cursor = conn.cursor()
    
    # query to create a database
    sql = ''' CREATE database products ''';
    
    # executing above query
    cursor.execute(sql)
    print("Database has been created successfully !!");
    