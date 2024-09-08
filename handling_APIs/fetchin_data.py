import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response =  requests.get(url).json()
    name = response['data']['name']['first']
    print(name)
    
fetch_random_user()