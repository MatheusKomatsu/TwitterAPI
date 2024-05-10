from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_SECRET, ACCESS_TOKEN
import tweepy
from constants import BRASIL_WOE_ID
from connection import trends_collection
def _get_trends(woe_id: int, api:tweepy.API) ->list[dict[str, any]]:
    """"
    Get Trending topics with Tweepy in Brazil
    """""

    trends = api.get_place_trends(woe_id)

    for tweet in trends:
        print(tweet.text)

    return trends[0]["trends"]

def get_trends_mongo()->list[dict[str,any]]:
    trends = trends_collection.find({})
    return list(trends)
@inject
def save_trends()->None :
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    trends = _get_trends(woe_id=BRASIL_WOE_ID, api=api)
    trends_collection.insert_many(trends)