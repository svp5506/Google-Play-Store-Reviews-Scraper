from bs4 import BeautifulSoup
import pandas as pd
import requests

URL = "https://play.google.com/store/apps/details?id=com.brighthouse.mybhn&hl=en_US&gl=US&pli=1"
r = requests.get(URL)
reviews = BeautifulSoup(r.content, 'lxml')  # Changed 'lxml' to 'html.parser'

androidReviews = []

for review in reviews.findAll('div', attrs={'class': 'h3YV2d'}):  # Updated class name to match the current structure
    androidReviews.append(review.text)  # Use .text to get the review text

dataframe = pd.DataFrame({'Reviews': androidReviews})  # Create a DataFrame with a 'Reviews' column

dataframe.to_csv('androidReviews.csv', index=False)
