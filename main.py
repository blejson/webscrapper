import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os
import re


def search_images():
    search = input("Search for:")
    params = {"q": search}
    dir_name = "scraped_images"
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    r = requests.get("https://www.google.pl/search?hl=pl&tbm=isch&source=hp&biw=1920&bih=938&q=plaza", params=params)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("img", {"class": "t0fcAb"})
    for item in links:
        print(item)
        url = item.attrs["src"]
        img_obj = requests.get(url)
        title = item.attrs["src"].split("/")[-1]
        title = re.sub('[,?=:&]', '', title)
        img = Image.open(BytesIO(img_obj.content))
        img.save("./" + dir_name + "/" + title+"."+img.format, img.format)
    search_images()


search_images()
