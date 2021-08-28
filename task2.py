import json
import requests
from bs4 import BeautifulSoup
# from task1 import scrape_top_movies

def group_by_year(movies):
    list=[]
    list1=[]
    for i in movies:
        list.append(i)
        if i["Year"] not in list1:
            list1.append(i["Year"])
    dict={}
    for k in list1:
        list2=[]
        for j in movies:
            year=j["Year"]
            if k==year:
                list2.append(j)
        dict[k]=list2
    with open("task2.json","w") as f:
        json.dump(dict,f,indent=4)
with open("task1.json","r") as f:
    data=json.load(f)
group_by_year(data)


    




