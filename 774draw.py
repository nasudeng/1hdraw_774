from requests_oauthlib import OAuth1Session
import schedule
import time
import datetime
import pickle
import json

def push_tweet(oa_session,twitext):
    url = "https://api.twitter.com/1.1/statuses/update.json"

    params = {"status":twitext}
    res = oa_session.post(url,params = params)

def kokuti_kaishi():
    oa_session = OAuth1Session(Consumer_key,Consumer_secret, Access_token, Access_secret)
    twitext = "開始の時間帯となりました。皆さま奮ってご参加ください！\n\n#774inc版深夜の真剣お絵描き60分一本勝負\n" + twiurl
    push_tweet(oa_session,twitext)
    print(str(datetime.datetime.now()) + "\n" + twitext)

def kokuti_owari():
    oa_session = OAuth1Session(Consumer_key,Consumer_secret, Access_token, Access_secret)
    twitext = "終了のお時間となりました。参加いただいた皆様、お疲れ様でした！\n\n#774inc版深夜の真剣お絵描き60分一本勝負"
    push_tweet(oa_session,twitext)
    print(str(datetime.datetime.now()) + "\n" + twitext)

def kokuti_odai():
    oa_session = OAuth1Session(Consumer_key,Consumer_secret, Access_token, Access_secret)
    talents = ["日ノ隈らん","因幡はねる","宗谷いちか","風見くく","柚原いづみ","灰原あかね","白宮みみ","羽柴なつみ","黒猫ななし","堰代ミコ","周防パトラ","島村シャルロット","西園寺メアリ","灰猫ななし","獅子王クリス","龍ヶ崎リン","虎城アンナ","三毛猫ななし","杏戸ゆげ","鴨見カモミ","季咲あんこ","花奏かのん"]

    dt_shokai = datetime.datetime(2020,4,28,23,30,00)
    dt_now = datetime.datetime.now()+datetime.timedelta(days=1)
    delta = (dt_now-dt_shokai).days+1

    i1,i2,i3 = rand_list[dt_now.day-1]
    twitext = "【第"+str(delta)+"回】"+str(dt_now.month)+"/"+str(dt_now.day)+"　22:00より開催\nお題は"+talents[i1]+"　"+talents[i2]+"　"+talents[i3]+"です！\n①チャレンジ精神・初心者歓迎\n②完成品はタグをつけて投稿\n#774inc版深夜の真剣お絵描き60分一本勝負"
    push_tweet(oa_session,twitext)
    print(str(datetime.datetime.now()) + "\n" + twitext)

    with open(rireki,mode="rb") as file:
        f = pickle.load(file)
    f.append([i1,i2,i3])
    with open(rireki,mode="wb") as file:
        pickle.dump(f)

def init(oa_session):
    url = "https://api.twitter.com/1.1/search/tweets.json"
    params = {"q":"from:@1hdraw_774ver exclude:retweets","result_type":"recent"}

    res = oa_session.get(url, params = params)
    json_file = json.loads(res.text)

    twiurl = "https://twitter.com/1hdraw_774ver/status/" + json_file["statuses"][0]["id_str"]

    url = "https://api.twitter.com/1.1/search/tweets.json"
    params = {"q":"#774inc版深夜の真剣お絵描き60分一本勝負 filter:images exclude:retweets","result_type":"recent"}

    res = oa_session.get(url, params = params)
    json_file = json.loads(res.text)

    id_list = []

    for read_line in json_file["statuses"]:
      id_list.append(read_line["id_str"])

    return twiurl,id_list

if __name__=="__main__":
    Consumer_key = ''
    Consumer_secret = ''
    Access_token = ''
    Access_secret = ''

    oa_session = OAuth1Session(Consumer_key,Consumer_secret, Access_token, Access_secret)


    with open("May2020",mode="rb") as f:
        rand_list = pickle.load(f)

    twiurl,id_list = init(oa_session)
    print(twiurl)

    schedule.every().day.at("22:00").do(kokuti_kaishi)
    schedule.every().day.at("23:00").do(kokuti_owari)
    schedule.every().day.at("23:30").do(kokuti_odai)

    print("this script is connected @1hdraw_774ver!")
    while True:
        schedule.run_pending()
        time.sleep(1)
