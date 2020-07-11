#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 23:00:05 2020

@author: joamila
"""

#Código desenvolvido para o tutorial disponível em: https://www.linkedin.com/pulse/como-obter-dados-da-api-do-twitter-inicia%25C3%25A7%25C3%25A3o-em-twython-joamila-brito/

from twython import Twython, TwythonStreamer

def get_trends_brazil(twitter):
    
    trends = twitter.get_place_trends(id=23424768)
    trds = trends[0]
    
    i = 0
    print ("---------TREND TOPICS BRASIL-------")
    for t in trds['trends']:
        if t['promoted_content'] != True:
            i += 1
            print("TT #", i, t['name'])

    return trds['trends'][0]


def get_some_tweets(twitter, key_phrase):
    
    print ("---------TWEETS RELEVANTES-------")
    for tweet in twitter.search(q=key_phrase)["statuses"]:
        user = tweet["user"]["screen_name"].encode('utf-8')
        user_name = tweet["user"]["name"].encode('utf-8')
        text = tweet["text"].encode('utf-8')
        
        print(user_name.decode('utf-8') + "(@" + user.decode('utf-8') + "): " + text.decode('utf-8'))
        
def get_stream_tweets(key_phrase):
    
    class MyStreamer(TwythonStreamer):
        def on_success(self, tweet):
            if tweet['user']['verified'] == True:
                usuario = tweet['user']['screen_name'].encode('utf-8')
                texto = tweet['text'].encode('utf-8')
                
                print(usuario.encode('utf-8'), ": ", texto.encode('utf-8'))
                
        def on_error(self, status_code):
            print(status_code)
            self.disconnect()
            
    print ("---------STREAM DE TWEETS-------")
    stream = MyStreamer(CONSUMER_KEY, SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream.statuses.filter(track=key_phrase)


twitter = Twython(CONSUMER_KEY, SECRET_KEY)

tt = get_trends_brazil(twitter)
get_some_tweets(twitter, tt['name'])
get_stream_tweets(tt['name'])
