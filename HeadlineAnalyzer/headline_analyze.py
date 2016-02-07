'''
Created on Feb 3, 2016

@author: akhil_rane
'''
import requests
import json
from lxml import html


class HeadlineAnalyzer: 
    
    urls = [ 'http://www.moneycontrol.com' ]
    api_key='d32fd35b1ab9112591c2b8d68b1397c6fa8526de'
    data={}
        
    def get_headlines(self):
        

        for url in self.urls:
            page = requests.get(url)
            tree = html.fromstring(page.content)
    
            headlines = []
            headlines += tree.xpath('//a[@class="bl_14"]/text()')
            headlines += tree.xpath('//a[@class="bl_18"]/text()')
            headlines += tree.xpath('//h1[@class="bl_20 dinline"]/text()')
        return headlines

        
    def get_headlines_analyze(self):
        
        
        for headline in self.get_headlines():
            headline = headline.strip(' \t\n\r')
     
            r = requests.post('http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment?apikey='+self.api_key+'&text='+headline+'&outputMode=json', 
                        headers = {
                  
            },    
  
            )
            
            j = json.loads(r.text)
            self.data[headline] = j['docSentiment']['type']         
#             
        return json.dumps(self.data)