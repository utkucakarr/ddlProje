from tiktokapipy.api import TikTokAPI
import pandas as pd
import json
import re
import string
import zeyrek
import nltk
from tqdm import tqdm
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

analyzer = zeyrek.MorphAnalyzer()
stop_words = set(stopwords.words('turkish'))

file_name = "tiktok_videos.json"
clean_file_name = "clean_tiktok_videos.json"
video_limit = 15
hashtag = "yeni yıl"

emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)


def write_json_file(this_file_name, tiktok_videos):
    with open(this_file_name, "w", encoding="utf-8") as out_file:
        json.dump(tiktok_videos, out_file, indent=4, ensure_ascii=False)

def formatter_text(text):
    # Construct string considering spaces within the list
    result = ''
    for item in text:
        if item == '':
            result += ' '  # Adding space for empty strings
        else:
            result += item

    return(result)

def clean_desc(tweets):
    tweet=[]
    nsw=[]

    for i, tweets_set in enumerate(tweets):
        for tweet_string in tqdm(tweets_set):  

            tweet_string = tweet_string.replace('\n','') #Line breaks lerden temizliyoruz
            tweet_string = re.sub('http://\S+|https://\S+', '', tweet_string) #tweetler içerisindeki linkler temizleniyor
            tweet_string = tweet_string.translate(str.maketrans("", "", string.punctuation)) #tweetlerdeki noktalama işaretleri temizleniyor
            tweet_string = emoji_pattern.sub(r'', tweet_string)  #tweet içerisindeki emojiler temizleniyor
            lemm_tweet = analyzer.lemmatize(tweet_string)  #tweetler için lemmatize işlemi gerçekleştiriliyor
            lemm_tweet=[el[1][-1] for el in lemm_tweet]
            for r in lemm_tweet:     
                if not r in stop_words: 
                    nsw.append(r)       #stopwords olmayanlar ayrılıyor ve aşağıda birleştiriliyor
                    
            clear_tweet =' '.join(nsw)  #dizi string hale getiriliyor
            nsw=[]
            clear_tweet = clear_tweet.lower() #bütün tweetler küçük harflere çevriliyor
            tweet.append(clear_tweet) #temizlenmiş tweetin kendisi listeye ekleniyor

    return tweet

def get_challenge_videos_scroll_down():
    # scroll down for 2.5 seconds when making requests
    with TikTokAPI(navigation_timeout=15.0) as api:
        challenge = api.challenge(hashtag)
        tiktok_videos = []
        for video in challenge.videos.limit(video_limit):
            tiktok_videos.append({
                "video_url": video.id,
                "video_desc": video.desc
            })
            
        # İlk veri kaydediliyor.
        write_json_file(file_name, tiktok_videos)

        # Veri temizleniyor.
        clean_videos = []
        for video in tiktok_videos:
            # Join non-empty elements with a space
            video["video_desc"] = formatter_text(clean_desc(video["video_desc"]))
            clean_videos.append(video)
        
        # Temizlenen veri kaydediliyor
        write_json_file(clean_file_name, clean_videos)


# testing
if(__name__ == '__main__'):
    get_challenge_videos_scroll_down()
