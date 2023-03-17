from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as settings
from config import config


def get_engine(parameters:dict) -> create_engine:
    keys = ['user', 'password', 'host', 'port', 'database']
    if not all(key in keys for key in parameters):
        raise Exception(f'Bad configuration settings, all keys must be included in the config file .ini Keys:{keys}')
    
    url = f"postgresql://{parameters['user']}:{parameters['password']}@{parameters['host']}:{parameters['port']}/{parameters['database']}"
    if not database_exists():
        create_database(url)
    
    engine = create_engine(url, pool_size=50, echo=False)
    return engine



def get_session() -> sessionmaker:
    engine = get_engine(config())
    session = sessionmaker(bind=engine)
    
    return session

session = get_session()
print(session)