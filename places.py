import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path) 
import random

places_api_key = os.environ.get("PLACES_API_KEY")


class Place():
    def __init__(self,name,lat,lon,addr):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.addr = addr
        
    def getName(self):
        return self.name
    
    def getLat(self):
        return self.lat
    
    def getLon(self):
        return self.lon
    
    def getAddr(self):
        return self.addr
    
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
        result_json = len(dataJson.get("results"))
        result_json = dataJson.get("results")[random.randint(0,result_json)]
        #result_json = dataJson.get("results")[0]
        print(result_json)
        try:
            self.name = result_json.get('name')
            self.lat = result_json.get("geometry").get("location").get("lat")
            self.lon = result_json.get("geometry").get("location").get("lng")
            self.addr = result_json.get("vicinity")
            print(self.getName())
            print(self.getLat())
            print(self.getLon())
            print("teste")
        except:
            self.name = 'Romana Restaurante e Pizzaria'#default
            self.lat = -23.4903232
            self.lon = -47.48873,13
            self.addr = "Av. São Paulo, 807 - Vila Haro, Sorocaba - SP, 18013-002"
 
    


