from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
from places import Place
chorme_options = webdriver.ChromeOptions()
chorme_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chorme_options.add_argument("--headless")
chorme_options.add_argument("--disable-dev-shm-usage")
chorme_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chorme_options)
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
import json

#driver = webdriver.Chrome(ChromeDriverManager().install())
class Page:
    
    
    def __init__(self,html):
        self.html = html
        
    def setHTML(self,html):
        self.html = html
    
    def getHTML(self,html):
        return self.html
    
    
    #search the page that contains all data that we want to crawling. This method need to be called by the crawling, passing the url.
    def perform(user_lat,user_lon):
        base = {"Opções de serviços":['Entrega sem contato','Entrega','Para viagem','Refeição no local','Mesas externas', 'Drive-through', 'Retirada na porta' ],
        "Saúde e segurança": ['Necessidade de fazer reserva','A equipe usa máscaras de proteção','É obrigatório usar máscara de proteção', 'Desinfecção das superfícies entre um cliente e outro'],
        "Comodidades":['Bom para levar crianças','Cadeirinhas altas','Banheiro','Wi-Fi gratuito'],
        "Acessibilidade": ['Banheiro com acessibilidade','Entrada com acessibilidade','Assento com acessibilidade','Estacionamento com acessibilidade'],
        "Pagamento": ['Cartões de débito','Pagamentos por dispositivo móvel via NFC','Cartões de crédito']}
        
        
        
        place = Place(name = 'default',lat = 'default',lon = 'default', addr='default')
        place.search_place(user_lat= user_lat, user_lon= user_lon, keyword='restaurante')
        print(place)
        
        name = place.getName() #name of the place near to the user
        adress = place.getAddr()
        print("chegou no nome: " + str(name))
        sliced_name = name.split(" ")
        nameAux = ""
        name = ""
        name_content = ""
        
        for i in sliced_name:
            nameAux += str(i) + "+"
        
        for i in range(len(nameAux)-1):
            name += nameAux[i]
            
        for i in sliced_name:
            name_content = i + " "
        
        
        lat_lon = '@' + str(place.getLat())+','+ str(place.getLon()) #cordinates
        driver.get("https://www.google.com/maps/search/"+ name +"/"+lat_lon+",15.25z") #first page will be changed by google
        
        time.sleep(5) #necessary to load all data in the page
        new_url = driver.current_url #getting the new changed URL
        driver.close
        print("novo url" + str(new_url))
        
        #completed URL that needs to be used for other chromedriver
        x_url = new_url.split("data=")
        y = x_url[1].split("!1s0")
        end_of_link = '!10e1'
        updated_URL = x_url[0] +"data=4m6!3m5!1s0" + y[1] + end_of_link
        driver.get(updated_URL)
        time.sleep(5)
        html_content = str(driver.page_source)    
        
        
        information = ""
        for i in base:
            for j in range(len(base[i])):
                if base[i][j] in html_content:
                    information += base[i][j] + "\n"

        data_content = {"name": name_content,
                        "Adress": adress,
                        "Information": information}
        
        return data_content
        
        
        

        
        

#driver.get("https://www.google.com.br/maps/place/Dicid/@-23.490331,-47.48873,13z/data=!4m10!1m2!2m1!1sdicid!3m6!1s0x94cf60339177292b:0xa942eaa90e9c0915!8m2!3d-23.5114806!4d-47.4354683!10e1!15sCgVkaWNpZCIDiAEBWgciBWRpY2lkkgELY2FuZHlfc3RvcmU")

