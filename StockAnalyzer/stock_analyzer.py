import requests
import json
import stockretriever

class StockAnalyzer: 
    
    
#    api_key='c11ce1bb1df578f16c09741b600f78e631903966' # rane co.in
#    api_key = '16993acf0f584867567e81501852794fe8bcc67f' # viren com
    api_key = 'b7c92242f995618a585f2cfd4128fbb20733a6e1' # sheldon ibm
    
        
    def get_stock_analyze(self,ticker):
        
        
        r = requests.post('http://gateway-a.watsonplatform.net/calls/data/GetNews?outputMode=json&start=now-1d&end=now&count=1&q.enriched.url.title='+ticker+'&return=enriched.url.title&apikey='+self.api_key,
                         headers = {

            },             )
        j = json.loads(r.text)
        try: 
            
            headline = j['result']['docs'][0]['source']['enriched']['url']['title']
            
            r = requests.post('http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment?apikey='+self.api_key+'&text='+headline+'&outputMode=json',
                         headers = {
             },
 
              )
 
            j1= json.loads(r.text)
            print j1
            return j1['docSentiment']['type']+','+j1['docSentiment']['score']
            
        except:
            news = stockretriever.get_news_feed(ticker)
            headlines=''
            for x in news:
                try:
  
                    headlines=headlines+x['title'].encode('utf-8')+'\n'
                except UnicodeEncodeError:
                        pass
            r = requests.post('http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment?apikey='+self.api_key+'&text='+headlines+'&outputMode=json',
                         headers = {
             },
 
              )
 
            j1= json.loads(r.text)
            print j1
            return j1['docSentiment']['type']+','+j1['docSentiment']['score']
                
        
