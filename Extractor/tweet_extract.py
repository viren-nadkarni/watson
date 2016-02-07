'''
Created on Feb 2, 2016

@author: akhil_rane
'''
import tweepy #https://github.com/tweepy/tweepy

class TweetExtractor:
    consumer_key = "9SvkB3kN9hyHGtsPxcqk4egig"
    consumer_secret = "YT4RrPbxEkTC2Z3SG7g6CUCvgmdfbFtR9JYdVecuDoVBAaqEIL"
    access_key = "235176044-o94ZaVDtussczaURWot7o4C8nJNg92CwyyVHOCOL"
    access_secret = "metYFVTHuqpua7CusLB60LVrPcB1hSheStmajt9FxyGAx"
    
    username=""
    def __init__(self,name):
        self.username=name
    
    def get_all_tweets(self):
        #Twitter only allows access to a users most recent 3240 tweets with this method
        
        #authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        api = tweepy.API(auth)
        
        #initialize a list to hold all the tweepy Tweets
        alltweets = []    
        
        #make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = api.user_timeline(screen_name = self.username,count=200)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        #keep grabbing tweets until there are no tweets left to grab
        print "Downloading tweets....." 
        while len(new_tweets) > 0:
                    
            #all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = self.username,count=200,max_id=oldest)
            
            #save most recent tweets
            alltweets.extend(new_tweets)
            
            #update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1
            
            
            if len(alltweets) >1000:
                print "Done!!!"
                break
        #transform the tweepy tweets into a 2D array that will populate the csv    
    #     outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    #      
    #     #write the csv    
    #     with open('%s_tweets.csv' % screen_name, 'wb') as f:
    #         writer = csv.writer(f)
    #         writer.writerow(["id","created_at","text"])
    #         writer.writerows(outtweets)
         
        pass
        
        result="" 
        
        for tweet in alltweets:
            result=result+"\n"+tweet.text.encode("utf-8")
            
        return result
        
        