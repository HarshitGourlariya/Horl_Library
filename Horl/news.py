import requests

def news(Content,Api_key):
    
    try:
        url =f"https://newsapi.org/v2/everything?q={Content}&apiKey={Api_key}"
        response = requests.get(url)
        result = response.json()
    except:
        result = "Error"
    return result

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


