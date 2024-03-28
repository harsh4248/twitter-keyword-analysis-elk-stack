import tweepy as tw
from datetime import datetime as dt
from elasticsearch import Elasticsearch
from tweety import Twitter
import datetime


SEARCH_TERM = 'Machine Learning'
def import_keys():
    '''
    Imports keys from the twitter.keys file returns list of api keys.
    '''
    key_location = 'twitter.keys'
    apikeys = []
    with open(key_location) as keys:
        for items in keys:
            apikeys.append(items.split('=')[1].strip(' ').strip('\n'))
        keys.close()
    
    return apikeys



def get_doc(tweet):
    '''
    Gets the tweet data and returns dictionary.
    tweet: tweet type var as 1st parameter 
    '''
    return {
        '@timestamp':datetime.datetime.now(),
        'tweet_date':tweet.created_on,
    # Tweet.author returns the user type object.
    # TODO: add author details below.
    'username': tweet.author.username,
    'account_creation_date':tweet.author.created_at,
    'user_description':tweet.author.description,
    'user_url': tweet.author.profile_banner_url,
    'verified_status': tweet.author.verified,
    'geo_enabled': tweet.author.location,
    'friends_count': tweet.author.friends_count,
    'followers_count': tweet.author.followers_count,
    'favorite_count': tweet.author.favourites_count,
    # TODO: add tweet details here
    'retweeted_count': tweet.retweet_counts,
    'hashtags': tweet.hashtags,
    'tweet_full_text':tweet.text}


def main():
    '''
    Main function
    '''
    # Importing keys 
    # apikeys = import_keys()
    # print(apikeys)
    # # Initialize dictionary
    # twitter_cred = dict()
    # # Enter API keys
    # twitter_cred["CONSUMER_KEY"] = apikeys[0]
    # twitter_cred["CONSUMER_SECRET"] = apikeys[1]
    # # Access Tokens
    # twitter_cred["ACCESS_KEY"] = apikeys[2]
    # twitter_cred["ACCESS_SECRET"] = apikeys[3]
    # auth = tw.OAuthHandler(consumer_key = twitter_cred["CONSUMER_KEY"],consumer_secret = twitter_cred["CONSUMER_SECRET"])
    # auth.set_access_token(twitter_cred["ACCESS_KEY"],twitter_cred["ACCESS_SECRET"])
    # # auth = tw.OAuth1UserHandler(consumer_key = twitter_cred["CONSUMER_KEY"], consumer_secret = twitter_cred["CONSUMER_SECRET"],
    #                             # access_token = twitter_cred["ACCESS_KEY"], access_token_secret = twitter_cred["ACCESS_SECRET"])
    # api = tw.API(auth, wait_on_rate_limit=True)
    # tweets = api.home_timeline()
    # for tweet in tweets:
    #     print(tweet)

    # Initialize elasticsearch node
    app = Twitter("session")
    app.start('harshdalwadi16', '+capb?kb_j.bV2Y')
    print(app.user)
    # all_tweets = app.get_tweets(app.get_user_info('elonmusk'))
    all_tweets = app.search(SEARCH_TERM, pages = 20)
    print(len(all_tweets))
    # for tweet in all_tweets:
    #   print(tweet.place)
    es = Elasticsearch(
    "https://localhost:9200/",
    basic_auth=("elastic", "nzXFRN921Q5uO40-G+CW"),
    ca_certs='/Users/harshdalwadi/Desktop/ELK Stack/elasticsearch-8.12.2/config/certs/http_ca.crt'
    )

    index_name = 'keyword_search' + '_' + datetime.datetime.today().strftime('%Y_%m_%d')

    for tweet in all_tweets:
        doc = get_doc(tweet)
        # print(doc)
        es.index(index = index_name, body = doc)




if __name__ == '__main__':
    main()
