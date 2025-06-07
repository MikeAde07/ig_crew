import requests
import json
import os



class SearchTools:
    def search(query, limit=5):
        

        url = "https://google.serper.dev/search"
        payload = json.dumps({
            "q": query,
            "num": limit,
        })
        headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json()['organic']

        
        