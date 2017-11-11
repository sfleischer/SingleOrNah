import numpy as np
import requests
import json


# queries azure sentiment api
def get_sentiment(posts):
    
    '''
    posts:
        [{
            language: 'en',
            id: some unique id,
            text: text to be analyzed
        }]

    '''

    url = 'https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '9da2b93062e44723aefba7df7e345820'
    }

    response = requests.post(url, data=str(posts).encode('utf-8'), headers=headers)
    print(response.json())
    try: 
        toReturn = {}
        for d in response.json()['documents']:
            toReturn[d['id']] = d['score']
        return toReturn
    except:
        return None

if __name__ == "__main__":
    posts = {
        "documents": [
            {
                "language": "en",
                "id": "1",
                "text": "We love this trail and make the trip every year. The views are breathtaking and well worth the hike!"
            },
            {
                "language": "en",
                "id": "2",
                "text": "Poorly marked trails! I thought we were goners. Worst hike ever."
            },
            {
                "language": "en",
                "id": "3",
                "text": "Everyone in my family liked the trail but thought it was too challenging for the less athletic among us. Not necessarily recommended for small children."
            },
            {
                "language": "en",
                "id": "4",
                "text": "It was foggy so we missed the spectacular views, but the trail was ok. Worth checking out if you are in the area."
            },                
            {
                "language": "en",
                "id": "5",
                "text": "This is my favorite trail. It has beautiful views and many places to stop and rest"
            }
        ]
    }
    print (get_sentiment(posts))