
###############################
# Source Code of @ShakirTheBot
# Author : Sali Kadir Chousein
# e-mail : sdi1200044@di.uoa.gr
###############################



import tweepy
import random
from time import sleep

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_KEY = ''
ACCESS_SECRET = ''

print('Starting Shakir...', flush = True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

my_file = open('pg44552.txt')

file_lines = my_file.readlines()

# close file

my_file.close()

FILE_NAME = 'last_seen_id.txt'

def retrive_last_seen_id (file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return




def reply():
    print('Reading Some Tweets and Replying if available')
    last_seen_id = retrive_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
    for mention in reversed(mentions):
        print(str(mention.id) + '-' + mention.full_text, flush = True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld')
            print('responding...')
            api.update_status('@' + mention.user.screen_name + '#helloworld back to you !', mention.id)
        elif 'how are you' in mention.full_text.lower():
            print('found mention type 2')
            print('responding...')
            api.update_status('@' + mention.user.screen_name + ' I am fine thanks!', mention.id)
        elif 'corona' in mention.full_text.lower():
            print('found mention type 3')
            print('responding...')
            api.update_status('@' + mention.user.screen_name + ' Stay home, stay safe', mention.id)
        elif 'i love ' in mention.full_text.lower() :
            print('found mention type 4')
            print('responding...')
            api.update_status('@' + mention.user.screen_name + ' Do you wanna drink something with me ? ', mention.id)
        elif 'nice to meet' in mention.full_text.lower() :
            print('found mention type 5')
            print('responding...')
            api.update_status('@' + mention.user.screen_name + ' Do you wanna drink something with me ? ', mention.id)
        elif 'fuck' in mention.full_text.lower() :
            print('found mention type 6')
            print('responding...')
            api.update_status('@' + mention.user.screen_name + ' I am gonna tell this to my boss @kadirchsalih ', mention.id)
        elif 'song' in mention.full_text.lower() :
            print('found mention type 7')
            print('responding...')
            api.update_status('@' + mention.user.screen_name + ' Mari Ye Kafani Mari Ye Kendini Ic Ic Kudur Kudur...', mention.id)
        elif 'life' in mention.full_text.lower() :
            print('found mention type 8')
            print('responding...')
            api.update_status('@' + mention.user.screen_name + ' Is Short', mention.id)
        elif 'hitler' in mention.full_text.lower() :
            print('found mention type 9')
            print('responding...')
            api.update_status('@' + mention.user.screen_name + ' choked by Rammstein', mention.id)

#######################################
def _tweet():
    for line in file_lines:


        try:
            print(line)
            if line != '\n':
                # Error Handling #
                api.update_status(line)
                reply()

                sleep(30)
                # Error Handling #
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(20)

while True :
    _tweet()


