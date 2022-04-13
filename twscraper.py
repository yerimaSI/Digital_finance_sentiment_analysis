# -*- coding: utf-8 -*-
import snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Params
file_path = "/home/rintiodev/wave_collect/data/"
date_debut = "2021-01-01"
date_fin = "2022-03-31"
wave_tags = ["#WavePay", "#Wave_Money", "#WaveMoney"]
mtn_tags = ["#MTNMoMo", "#MTNMoMoAdvance", "#JustMoMoIt"]
orange_tags = ["#OrangeMoney", "#OrangeMoneyAfrica"]

def save_data(df, name):
    df.to_csv(file_path + name + ".csv")

def get_tweets(search_word, limit=None):
    liste = []
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for word in search_word:
        query = word + " since:" + date_debut + " until:" + date_fin
        print(query)
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            liste.append([
                tweet.id, 
                tweet.date, 
                tweet.content, 
                tweet.renderedContent, 
                tweet.user.username, 
                tweet.user.displayname, 
                tweet.url, 
                tweet.hashtags
            ])
            if limit and i>=limit:
                break
    return pd.DataFrame(liste, columns=[
        "ID",
        "DATE",
        "TEXT",
        "RENDERED_TEXT",
        "USERNAME",
        "DISPLAYNAME",
        "URL", 
        "TAGS"
    ])

wave_df = get_tweets(wave_tags)
mtn_df = get_tweets(mtn_tags)
orange_df = get_tweets(orange_tags)

print("COLLECT DATA:...  \n  Wave: {}  \n  Orange Money: {} \n  Mtn MoMo {}".format(len(wave_df),len(mtn_df), len(orange_df)))

save_data(wave_df, "wave")
save_data(mtn_df, "mtn")
save_data(orange_df, "orange")
