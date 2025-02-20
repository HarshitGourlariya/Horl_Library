import requests
import json
from tabulate import tabulate


def news(Content, Api_key):
    try:
        response = requests.get(f"https://newsapi.org/v2/everything?q={Content}&apiKey={Api_key}")
        response.raise_for_status()
        data = response.json()

        table_data = []
        for article in data.get('articles', []):
            title = article.get('title', "Error")
            date = article.get('publishedAt', 'N/A')
            url = article.get('url', 'N/A')
            description = article.get('description', 'N/A')
            source = article.get('source', {}).get('name', 'N/A')

            table_data.append([title, date, url, description, source])

        headers = ["Title", "Date", "URL", "Description", "Source"]
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def Country(Country,Api_key):
    try:
        url = f"https://api.worldnewsapi.com/top-news?source-country={Country}&language=en&date=2024-05-29"
        api_key = Api_key

        headers = {
            'x-api-key': api_key
        }

        response = requests.get(url, headers=headers)
        result = response.json()
    except:
        result = "Error"
    return result








