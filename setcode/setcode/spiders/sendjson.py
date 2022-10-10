
import scrapy
import requests
import json

class SendJson(scrapy.Spider):
    name = 'sendjson'
    llowed_domains = ['yugipedia.com']
    start_urls = ['https://yugipedia.com/wiki/Legendary_Hero_Decks']              
    
    user = {'username': 'alannaicson','password': '91628319'}
    
    resp = requests.post('http://localhost:8080/yugiohAPI/auth/login', json = user)
    data = resp.json();
    token = data['accessToken']
    auth ='Bearer '+token              
    
    def parse(self, response):
        
        path = "setcode.json"
        with open(path, 'r') as j:    
            json_payload = json.loads(j.read())   
            requests.post('http://localhost:8080/yugiohAPI/decks/update-cards-quantity', headers={"Authorization": SendJson.auth}, json = json_payload)
        
        pass
    



       