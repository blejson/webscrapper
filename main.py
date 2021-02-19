import requests

search = input("Search for:")
params = {"q": search}
r = requests.get("https://www.bing.com/images/search", params=params)

print(r.text)
