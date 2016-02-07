import requests
import json
import stockretriever

class StockAnalyzer: 
    
    
    api_key='d32fd35b1ab9112591c2b8d68b1397c6fa8526de'
    
        
    def get_stock_analyze(self,ticker):
        
        
        r = requests.post('https://gateway-a.watsonplatform.net/calls/data/GetNews?outputMode=json&start=now-1d&end=now&count=1&q.enriched.url.title='+ticker+'&return=enriched.url.title&apikey='+self.api_key,
                verify=False,
                         headers = { },             )
        j = json.loads(r.text)
        try: 
            
            headline = j['result']['docs'][0]['source']['enriched']['url']['title']
            
            r = requests.post('http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment?apikey='+self.api_key+'&text='+headline+'&outputMode=json',
                verify=False,
                         headers = {
             },
 
              )
 
            j1= json.loads(r.text)
            return j1['docSentiment']['type']
            
        except:
            news = stockretriever.get_news_feed(ticker)
            headlines=''
            for x in news:
                try:
  
                    headlines=headlines+x['title'].encode('utf-8')+'\n'
                except UnicodeEncodeError:
                        pass
            r = requests.post('http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment?apikey='+self.api_key+'&text='+headlines+'&outputMode=json',
                verify=False,
                         headers = {
             },
 
              )
 
            j1= json.loads(r.text)
            print j1
            return j1['docSentiment']['type']
                
        
