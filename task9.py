import random
import  time
import requests
from bs4 import BeautifulSoup
import json
import os
from task1 import scrape_top_movies
from task5 import  get_movie_list_details


with open("task5.json","r") as f:
    m_data=json.load(f)

movie = m_data
# print(movie)
def get_movie_details(movie):
    for i in movie:
        random_sleep=random.randint(1,3)
        path=open("/home/dell/Desktop/webscraping/9.text"+i["Moviename"]+".text","w")
        m_data=str(i)
        create=path.write(m_data)
        time.sleep(random_sleep)
        path.close()
        # print(path)

get_movie_details(movie)




# def get_movie_list_details(movie):
#     random_sleep=random.randint(1,3)
#     movie_list = []
#     for i in movie:
#         path="/home/dell/Desktop/webscraping/9.text"+i["Moviename"]+".text"
#         if os.path.exists("file.json"):
#             # print(path)
#             pass
#         else:
#             create=open("/home/dell/Desktop/webscraping/9.text"+i["Moviename"]+".text","w")
#             # print(create)
#             create=open(i["Moviename"]+".text","w")
#             url=requests.get(i["Movieurl"])
#             create1=create.write(url.text)
#             create.close()
#             a=scrape_top_movie((i["Moviename"],i["Movieurl"]))
#             movie_list.append(a)
#             time.sleep(random_sleep)
#     print(movie_list)

# get_movie_list_details(movie)
