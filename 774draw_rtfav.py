from requests_oauthlib import OAuth1Session
import schedule
import time
import datetime
import pickle
import json


def init(oa_session):
    url = "https://api.twitter.com/1.1/search/tweets.json"
    params = {"q":"#774inc版深夜の真剣お絵描き60分一本勝負 filter:images exclude:retweets","result_type":"recent"}

    res = oa_session.get(url, params = params)
    json_file = json.loads(res.text)

    id_list = []

    for read_line in json_file["statuses"]:
      id_list.append(read_line["id_str"])

    return id_list

def search(oa_session,rted_list):
  url = "https://api.twitter.com/1.1/search/tweets.json"
  params = {"q":"#774inc版深夜の真剣お絵描き60分一本勝負 filter:images exclude:retweets","result_type":"recent"}

  res = oa_session.get(url, params = params)
  json_file = json.loads(res.text)

  id_list = []

  for read_line in json_file["statuses"]:
    id_list.append(read_line["id_str"])

  return id_list

def rt(oa_session,tweet_id):
  url = "https://api.twitter.com/1.1/statuses/retweet/" + tweet_id +".json"
  res = oa_session.post(url)
  print(res)

def fav(oa_session,tweet_id):
  url = "https://api.twitter.com/1.1/favorites/create.json?id=" + tweet_id
  res = oa_session.post(url)
  print(res)

def rtandfav():

    while(True):
        rted_list = search(oa_session,id_list)
        for i in range(len(rted_list)):
            print(rted_list[i])
            if not(rted_list[i] in id_list):
                print(rted_list[i] + "\007")
                rt(oa_session,rted_list[i])
                fav(oa_session,rted_list[i])
                id_list.append(rted_list[i])
        time.sleep(wt)

if __name__=="__main__":
    Consumer_key = ''
    Consumer_secret = ''
    Access_token = ''
    Access_secret = ''

    oa_session = OAuth1Session(Consumer_key,Consumer_secret, Access_token, Access_secret)


    id_list = init(oa_session)

    wt = int(input())


    rtandfav()
