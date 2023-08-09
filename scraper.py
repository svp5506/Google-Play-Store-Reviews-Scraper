from bs4 import BeautifulSoup
import pandas as pd
import requests

URL = "https://play.google.com/store/apps/details?id=com.brighthouse.mybhn&hl=en_US&gl=US&pli=1"
r = requests.get(URL)
reviews = BeautifulSoup(r.content, 'html.parser')

androidReviews = []

for _ in range(10):  # Scroll 10 times (adjust as needed)
    for review in reviews.find_all('div', attrs={'class': 'h3YV2d'}):
        androidReviews.append(review.get_text(strip=True))

    # Find the last review on the page
    last_review = reviews.find('div', attrs={'class': 'h3YV2d'})
    
    if last_review:
        order_value = last_review.get('data-order-value', 0)
        
        # Construct the URL for the next page of reviews
        next_url = f"{URL}&reviewSortOrder=2&reviewType=1&pageNum={order_value}"
        
        r = requests.get(next_url)
        reviews = BeautifulSoup(r.content, 'html.parser')
    else:
        break

df = pd.DataFrame({'Reviews': androidReviews})

df.to_csv('androidReviews.csv', index=False)
