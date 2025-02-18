import requests

def news(Content,Api_key):
    
    try:
        url =f"https://newsapi.org/v2/everything?q={Content}&apiKey={Api_key}"
        response = requests.get(url)
        result = response.json()
    except:
        result = "Error"
    return result
