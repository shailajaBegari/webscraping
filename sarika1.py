import json
import requests
from bs4 import BeautifulSoup
from task1 import scrape_top_list
# file=open("mytask1.json","r")
# movies=json.load(file)

def group_by_year(movies):
    year_dict={}
    for i in movies:
        main_list=[]
        for j in movies:
            if i["year"]==j["year"]:
                main_list.append(j)
                year_dict[i["year"]] =main_list
    with open("task2.json","w+") as file:
        json.dump(year_dict,file,indent=4)        
        check=json.dumps(year_dict,indent=4) 
    # print( main_list)   
    return year_dict

group_by_year(movies=scrape_top_list())

