import urllib.request
import json
import time

serviceURL = "https://v2.jokeapi.dev/joke"


jokeCategory = input("Select Joke category from - Programming, Misc, Dark, Pun, Spooky, Christmas\n")
serviceURL = serviceURL + "/" + jokeCategory

isNSFW = input("Should joke not be NSFW? y/n\n")
if (isNSFW == "y" ):
    serviceURL += "?blacklistFlags=nsfw"
isReligious = input("should the joke not be religious? y/n\n")
if(isReligious == "y"):
    if(serviceURL.find("?blacklistFlags")):
        serviceURL += "," + "religious"
    else:
        serviceURL += "?blacklistFlags=religious"

print("retrieving", serviceURL)
urlRequest = urllib.request.urlopen(serviceURL)
jsonReady = urlRequest.read().decode()
jokeJSON = json.loads(jsonReady)

if jokeJSON['type'] == "single":
    print(jokeJSON['joke'])
else:
    print(jokeJSON['setup'])
    time.sleep(3)
    print(".... ..... ....")
    time.sleep(3)
    print(jokeJSON['delivery'])
