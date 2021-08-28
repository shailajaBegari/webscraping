import json
import requests
from bs4 import BeautifulSoup
# from task1 import scrape_top_movies

def group_by_year(movies):
    list=[]
    list1=[]
    for i in movies:
        list.append(i)
    # print(list)
        if i["Year"] not in list1:
            list1.append(i["Year"])
    # print(list1)
    dict={}
    for k in list1:
        list2=[]
        for j in movies:
            year=j["Year"]
            if k==year:
                list2.append(j)
    # print(list2)
        # dict[k]=list2
        var_a=k//10
        var_b=str(var_a)+str(0)
        dict[var_b]=list2
    with open("task3.json","w") as f:
        json.dump(dict,f,indent=4)
with open("task1.json","r") as f:
    data=json.load(f)
group_by_year(data)


    




