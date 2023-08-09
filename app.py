from google_play_scraper import Sort, reviews_all
import pandas as pd

result = reviews_all(
    'com.brighthouse.mybhn',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
)

reviews = result['reviews']
df = pd.DataFrame(reviews)

df.to_csv('androidReviews.csv',index=False)