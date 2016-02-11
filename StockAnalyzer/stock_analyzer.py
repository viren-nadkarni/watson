import requests
import json
import stockretriever
import random

class StockAnalyzer: 
    
    
    api_key = [ 'c11ce1bb1df578f16c09741b600f78e631903966', '16993acf0f584867567e81501852794fe8bcc67f', 'b7c92242f995618a585f2cfd4128fbb20733a6e1']
#    api_key='c11ce1bb1df578f16c09741b600f78e631903966' # rane co.in
#    api_key = '16993acf0f584867567e81501852794fe8bcc67f' # viren com
#    api_key = 'b7c92242f995618a585f2cfd4128fbb20733a6e1' # sheldon ibm
#    api_key = 'be3851c72c78c390ce3a3cdea6056f3cc02627fa' # viren co.in
    
        
    def get_stock_analyze(self,ticker):
        
        
        r = requests.post('http://gateway-a.watsonplatform.net/calls/data/GetNews?outputMode=json&start=now-1d&end=now&count=1&q.enriched.url.title='+ticker+'&return=enriched.url.title&apikey='+random.choice(self.api_key),
                         headers = {

            },             )
        j = json.loads(r.text)
        try: 
            
            headline = j['result']['docs'][0]['source']['enriched']['url']['title']
            
            r = requests.post('http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment?apikey='+random.choice(self.api_key)+'&outputMode=json'+'&text='+headline,
                         headers = {
             },
 
              )
 
            print ticker, r.text
            j1= json.loads(r.text)
            return j1['docSentiment']['type']+','+j1['docSentiment']['score']
            
        except:
            news = stockretriever.get_news_feed(ticker)
            headlines=''
            for x in news:
                try:
                    headlines=headlines+x['title'].encode('utf-8')+'\n'
                except UnicodeEncodeError:
                    pass
            r = requests.post('http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment?apikey='+random.choice(self.api_key)+'&outputMode=json'+'&text='+headlines,
                         headers = {
             },
 
              )
 
            print ticker, r.text
            j1= json.loads(r.text)
            return j1['docSentiment']['type']+','+('0' if j1['docSentiment']['type'] == 'neutral' else j1['docSentiment']['score'])
                
        
