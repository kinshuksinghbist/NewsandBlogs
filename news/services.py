import requests
import os
from dotenv import load_dotenv
load_dotenv()

class NewsService:

    NEWS_API_KEY = os.getenv('NEWS_API_KEY')
    BASE_URL = 'https://newsapi.org/v2/top-headlines'

    @classmethod
    def get_news_articles(cls, country='us', category='technology'):
        params = {
            'apiKey': cls.NEWS_API_KEY,
            'country': country,
            'category': category
        }
        response = requests.get(cls.BASE_URL, params=params)
        return response.json().get('articles', [])
