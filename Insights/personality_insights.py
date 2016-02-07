'''
Created on Feb 2, 2016

@author: akhil_rane
'''

from Extractor import tweet_extract

import requests
import json


class PersonalityInsights:
    
    tweets=""
    def __init__(self,name):  
        
        tool=tweet_extract.TweetExtractor(name)
        self.tweets=tool.get_all_tweets()
        
    def get_insights(self):
        
        
        r = requests.post('https://gateway.watsonplatform.net/personality-insights/api/v2/profile', 
            auth=('b74fc1cc-a434-4dff-9504-0d11c8822b43','Q1sqKtUpuAy6'),
            headers = {
                'content-type': 'text/plain',
                'accept': 'application/json'
            },
            data=self.tweets
        )
        print("Profile Request sent. Status code: %d, content-type: text/plain" )       
      
        
        j = json.loads(r.text)    
        
        adventurousness=j['tree']['children'][0]['children'][0]['children'][0]['children'][0]['percentage']
        liberalism=j['tree']['children'][0]['children'][0]['children'][0]['children'][5]['percentage']
        cautiousness=j['tree']['children'][0]['children'][0]['children'][1]['children'][1]['percentage']
        anxiety = j['tree']['children'][0]['children'][0]['children'][4]['children'][1]['percentage']
        challenge = j['tree']['children'][1]['children'][0]['children'][0]['percentage']
        practicality = j['tree']['children'][1]['children'][0]['children'][8]['percentage']
        
        
        risk_score = "{0:.2f}".format(round(((adventurousness+challenge+liberalism)/3)-((anxiety+practicality+cautiousness)/3),2))
      
        data = {}
        data['risk_score'] = risk_score        
            
        return json.dumps(data)