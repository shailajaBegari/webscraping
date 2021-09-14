import json
import requests
from bs4 import BeautifulSoup
from task5 import  get_movie_list_details

with open("task5.json","r") as f:
    data=json.load(f)


movie_info=data[:10]
# print(data)
    
def analyse_movies_genre():
    gener_list=[]
    for i in movie_info:
        gener_list.append(i["Genre"])
    print(gener_list)
    s_l=[]
    for i in gener_list:
        if type(i)==list:
            for j in i:
                s_l.append(j)
    # print(s_l)

    r_c=[]
    for i in s_l:
        str=""
        for j in i:
            if j==" ,":
                pass
            else:
                str+=j
        r_c.append(str)
    w_d=[]
    for i in r_c:
        if i not in w_d:
            w_d.append(i)
    # print(w_d)
    w_d_l=[]
    for i in w_d:
        if i=="&":
            pass
        else:
            w_d_l.append(i)

    main_dict={}
    for i in w_d_l:
        c=0
        for j in r_c:
            if i==j:
                c=c+1
        main_dict[i]=c
    # print(main_dict)
    with open("task11.json","w") as f:
        json.dump(main_dict,f,indent=4)

analyse_movies_genre()
