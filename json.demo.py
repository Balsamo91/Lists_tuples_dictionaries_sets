# pip3 install requests to install the module
import requests

respone = requests.get("https://swapi.dev/api/films/1")

print(respone.json())

respone_dict = respone.json()

# print(type(respone_dict))

print(respone_dict.keys())

respone_dict.pop("opening_crawl")
respone_dict.pop("planets")
respone_dict.pop("starships")
respone_dict.pop("vehicles")
respone_dict.pop("species")
respone_dict.pop("url")
respone_dict.pop("characters")

print(respone_dict)