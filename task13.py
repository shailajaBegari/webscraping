import json

with open("task4.json","r") as f:
    d1=json.load(f)


with open("task12.json","r") as f:
    d2=json.load(f)

def  scrape_movie_cast(data1,data2):
    dic=data1
    for cast in data2.values():
        dic["CAST"]=cast

    with open("task13.json","w") as f:
        json.dump(dic,f, indent=4)

scrape_movie_cast(d1,d2)
