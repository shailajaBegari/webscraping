import json
import requests
from bs4 import BeautifulSoup
from task5 import get_movie_list_details

with open("task5.json","r") as f:
    m_data=json.load(f)

data=m_data
def analyse_movies_directors():
    li=[]
    for i in data:
        if i["Director"] not in li:
            li.append(i["Director"])
    i=0
    l=[]
    while i<len(li):
        j=0
        while j<len(li[i]):
            l.append(li[i][j])
            j=j+1
        i=i+1
    # print(l)
    var=l
    var.insert(11,var[11][:-1])
    var.pop(12)

    d={}
    for i in var:
        c=0
        for j in var:
            if i==j:
                c=c+1
        d[i]=c
    # print(d)
    with open("task7.json","w") as f:
        json.dump(d,f,indent=4)

analyse_movies_directors()






