import requests
import json
from authentication import auth

bearerToken = auth()

def geturl():
    userID = "969139709023629313"
    url = "https://api.twitter.com/2/users/" + userID + "/following"

    return url

def main():
    url = geturl()
    bearerToken = auth();
    response = requests.request("GET",url,headers={"Authorization" : f"Bearer {bearerToken}"})
    jsonOP = response.json()
    for user in jsonOP['data']:
        print(user['name'])

if __name__ == '__main__':
    main()