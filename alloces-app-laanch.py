import tweepy
import os # operating system library

def create_api():
  consumer_key = 'WUofRtH7LvYwjhlCZmb4sgjaL'
  consumer_secret = 'ls0lcwtbi2iiDR1LueEM5e1sYI5CDavqR04G245cPojJDqzz96'
  access_token = '1297365763297177600-EGwQHlkfrJ8tiIVxnhnr9Zm9N3Oexs'
  access_token_secret = 'VyryFOfwqPAwDi5lXNQr8mPDD1Y4kEh5f8DcPKFOMULW1'

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print('API Created')
  return api
  
# Complete code
import time

def follower_count(user):
  emoji_numbers =  {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                      4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

  uf_split = [int(i) for i in str(user.followers_count)]

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()]) 
  return emoji_followers

api = create_api()

while True:
    user = api.get_user('Alloces0')
    api.update_profile(name=f'Alloces|{follower_count(user)} Followers')
    print(f'Updating Twitter Name : Alloces|{follower_count(user)} Followers')
    print('Waiting to refresh')
    time.sleep(60)
    
    
