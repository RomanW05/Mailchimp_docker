import httpagentparser
import geocoder
from config import geolocation_agent
from geopy.geocoders import Nominatim

def strip_user_agent(user_agent:str) -> dict:
    json_data = httpagentparser.detect(user_agent)
    os = f"{json_data['os']['name']} {json_data['os']['version']}"
    browser = f"{json_data['browser']['name']} {json_data['browser']['version']}"
    
    return os, browser

def json_parameters_extractor(json_parameters):
    subscriber_id = json_parameters['subscriber_id']
    template_id = json_parameters['template_id']
    campaign_id = json_parameters['campaign_id']

    return subscriber_id, template_id, campaign_id


def location_extractor(ip):
    if ip == '127.0.0.1':
        return 'localhost home', 'localhost home'
    g = geocoder.ip(ip)
    geolocator = Nominatim(user_agent=geolocation_agent()['agent_number'])
    location = geolocator.reverse(f"{g.latlng[0]}, {g.latlng[1]}", language='en')
   
    locator = geolocator.geocode(location.address, addressdetails=True)
    city = locator.raw['address']['town']
    country = locator.raw['address']['country']

    return city, country

