import scrapy
import requests
import json

class CardsetcodeSpider(scrapy.Spider):
    
    name = 'cardsetcode'
    llowed_domains = ['yugipedia.com']
    print("Infome a url: ")
    url = str(input())
   ## start_urls = ['https://yugipedia.com/wiki/Legendary_Hero_Decks']   
    start_urls = [url]           
    
    def parse(self, response):
        for infos in response.css('.wikitable tr'):
            yield{
                'setcode': infos.css('td:nth-child(1) a::text').get(),
                'quantity': infos.css('td:nth-child(6)::text').get()        
            }
        pass

    



       