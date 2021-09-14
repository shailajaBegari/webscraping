import requests
from bs4 import BeautifulSoup
import json
import os
from task1 import scrape_top_movies
from task4 import  scrape_top_movie

with open("task1.json","r") as f:
    m_data=json.load(f)

movie = m_data
def get_movie_list_details(movie):
    movie_list = []
    for i in movie:
        path="/home/dell/Desktop/webscraping/2.txt"+i["Moviename"]+".text"
        if os.path.exists("file.json"):
            # print(path)
            pass
        else:
            create=open("/home/dell/Desktop/webscraping/2.txt"+i["Moviename"]+".text","w")
            
            url=requests.get(i["Url"])
            create1=create.write(url.text)
            create.close()

get_movie_list_details(movie)
