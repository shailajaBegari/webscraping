import  json 
import requests
from bs4 import BeautifulSoup

movie_url="https://www.rottentomatoes.com/m/toy_story_4"
movie_name=" Toy Story 4  "

def  scrape_movie_details(movie_url ):
    res=requests.get(movie_url)
    soup=BeautifulSoup(res.text,'html.parser')
    d={}

    maindiv=soup.find_all("li",class_="meta-row clearfix")
    d["MOVIE NAME"]=movie_name
    d["MOVIE URL"]=movie_url
    for v in maindiv:
        x=v.get_text().strip()
        y=x.split()
        # print(y)
        # d={}
        # d["MOVIE NAME"]=movie_name
        # d["MOVIE URL"]=movie_url
        if y[0]=="Rating:":
            d["RATING"]=y[1]
        # print(d)
        elif y[0]=="Genre:":
            b=[]
            for i in y:
                if i!="Genre:":
                    a=i.strip()
                    b.append(a)
                d["GENUR"]=b
            # print(d) 
        elif y[1]=="Language:":
            d[" ORIGINAL LANGUAGE"]=[y[2]]
            # print(d)
        elif y[0]=="Director:":
            di=[]
            for i in y:
                if i!="Director:":
                    di.append(i)
                d["DIRECTOR"]=di
            # print(d)
        elif y[0]=="Producer:":
            p=[]
            for i in y:
                if i!="Producer:":
                    p.append(i)
                d["PRODUCER"]=p
            # print(d)
        elif y[0]=="Writer:":
            w=[]
            for i in y:
                if i!="Writer:":
                    w.append(i)
                d["WRITER"]=w
            # print(d)
        elif y[0]=="Runtime:":
            r=[]
            for i in y:
                if i!="Runtime:":
                    a=i.strip()[:-1]
                    r.append(a)
            # print(r)
            a=int(r[0])
            # print(a)
            con=a*60
            b=int(r[1])
            sum=con+b
            d["RUNTIME"]=sum
        # print(d)
        elif y[0]=="Distributor:":
            D=[]
            for i in y:
                if i!="Distributor:":
                    D.append(i)
                d["DISTRIBUTOR"]=D
            # print(d)
    with open("task4.json","w") as f:
        json.dump(d,f,indent=4)
    

scrape_movie_details(movie_url)





















