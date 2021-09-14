import requests
import json
from bs4 import BeautifulSoup
from task1 import scrape_top_movies
from task4 import scrape_top_movie

with  open("task5.json","r") as f:
    data=json.load(f)
# print(data)
# s_data=data

def  analyse_language_and_directors():
    dic={}
    for i in data:
        # print(i)
        for Director in i["Director"]:
            # print(Director)
            dic[Director]={}
        # print(dic)
    for i in range(len(data)):
        for Director in dic:
            if  Director in data[i]["Director"]:
                for  Language  in data[i]["Language"]:
                    dic[Director][Language]=0
        # print(dic)
    for i in range(len(data)):
        for Director in dic:
            if  Director in data[i]["Director"]:
                for Language  in data[i]["Language"]:
                    dic[Director][Language]+=1
        # print(dic)
        with open("task10.json","w") as f:
            json.dump(dic,f,indent=4)


    return dic
    
analyse_language_and_directors()




