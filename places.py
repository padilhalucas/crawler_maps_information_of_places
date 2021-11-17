import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path) 

places_api_key = os.environ.get("PLACES_API_KEY")


class Place():
    def __init__(self,name,lat,lon):
        self.name = name
        self.lat = lat
        self.lon = lon 
        
    def getName(self):
        return self.name
    
    def getLat(self):
        return self.lat
    
    def getLon(self):
        return self.lon
    
    def setName(self,name):
        self.name = name
    
    def setLat(self,lat):
        self.name = lat
    
    def setLon(self,lon):
        self.name = lon
        
    
    def search_place(self,user_lat,user_lon,keyword):
        
        try:
            url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+user_lat + "%2C" +  user_lon + "&radius=1500&type=restaurant&keyword=" + keyword+"&key=" + places_api_key
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload) #default
        except: 
            url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-23.4903232%2C47.48873,13&radius=1500&type=restaurant&keyword=" + keyword+"&key=" + places_api_key
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
        
        
        dataJson = response.json()
        result_json = dataJson.get("results")[1]
        
        try:
            self.setName(result_json.get('name'))
            self.setLat(result_json.get("geometry").get("location").get("lat"))
            self.setLon(result_json.get("geometry").get("location").get("lat"))
        except:
            self.setName('Romana Restaurante e Pizzaria') #default
            self.setLat(-23.4903232)
            self.setLon(-47.48873,13)
 
    


