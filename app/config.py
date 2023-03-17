#!/usr/bin/python
from configparser import ConfigParser
from pathlib import Path
import os

current_file_path = os.path.dirname(os.path.abspath(__file__))

def config(filename=f'{current_file_path}/.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db



def encoder(filename=f'{current_file_path}/.ini', section='encoder'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to encoder
    encode_keys = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            encode_keys[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return encode_keys


def geolocation_agent(filename=f'{current_file_path}/.ini', section='nominatim'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to encoder
    agent = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            agent[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return agent


def email_credentials(filename=f'{current_file_path}/.ini', section='email'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to encoder
    email_data = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            email_data[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return email_data