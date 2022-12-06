import tweepy
import config
import csv
import pandas as pd


client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

filename = "TwitterApiResult.csv"

query = 'QATAR OR QATAR2022 -is:retweet'

response = client.search_recent_tweets(query=query, max_results=10, user_fields=['username','profile_image_url'], expansions=['author_id'])

users = {u['id']: u for u in response.includes['users']}

for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        """
        print(tweet.id)
        print(user.username)
        print(user.profile_image_url)
        print(tweet.text)
        """
        print(f'tweetID:{tweet.id}')
        print(f'Username:{user.username}')
        print(f'Tweet text:{tweet.text}')
        print(f'ProfileImage:{user.profile_image_url}')
        

        



# csv code
fields = ['twitterID','twitterUsername', 'twitterText']
rows = []

for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        row = [tweet.id, user.username, tweet.text]
        rows.append(row)

print('abc')
print(rows)
# with open(filename,'w') as csvfile:

#     csvwriter = csv.writer(csvfile)
    
#     csvwriter.writerow(fields)
#     csvwriter.writerows(rows)

with open(filename,'w',encoding="utf-8") as f:

    csvWr = csv.writer(f)
    
    csvWr.writerow(fields)
    csvWr.writerows(rows)


a = pd.read_csv("TwitterApiResult.csv")

a.to_html("output.html")

