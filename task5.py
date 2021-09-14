import json
import requests
from bs4 import BeautifulSoup
from task1 import  scrape_top_movies
from task4 import  scrape_top_movie
with open("task1.json","r") as f:
    movie_url=json.load(f)
    
ten_movie=movie_url[:50]
# print(ten_movie)

def get_movie_list_details():
    list_url=[]
    for i in ten_movie:
        for j in i:
            if j=="Url":
                list_url.append(scrape_top_movie(i["Url"]))            
        with open("task5.json","w") as f:
            json.dump(list_url,f,indent=4)

get_movie_list_details()