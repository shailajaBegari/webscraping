import json
import requests
from  task5 import get_movie_list_details

with open("task5.json","r") as f:
    data=json.load(f)
# print(data)


def analysis_movie_language():
    d={}
    count=0
    for i in data:
        if i["Language"]==["English"]:
            count=count+1
        else:
            pass
    d["language"]=count

    with open("task6.json","w") as f:
        json.dump(d,f,indent=4)
    # return d

analysis_movie_language()







