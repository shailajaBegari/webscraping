import json
import requests
from bs4 import BeautifulSoup
result=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")
soup=BeautifulSoup(result.text,"html.parser")
print(soup)
def scrape_top_list():
    list1=[]
    mainDiv=soup.find("div",class_="lister")
    tableBody= mainDiv.find("tbody",class_="lister-list")
    allTrs= tableBody.find_all('tr')
    position=1
    for i in allTrs:
        # print(i)
        newDict={}
        allTds= i.find_all('td')
        for j in allTds:
            movieName=i.find('td',class_="titleColumn").a.get_text()
            newDict["movieName"]=movieName
            year=i.find('td',class_="titleColumn").span.get_text()
            newDict["year"]=int(year[1:5])
            rating=i.find('td',class_="imdbRating").get_text()
            newDict["rating"]=float(rating)
            url=i.find('td',class_="titleColumn").a["href"]
            url_add="https://www.imdb.com"+url
            # url_add="https://www.imdb.com/title/tt0048473/"
            newDict["url_add"]=url_add
            # print(year)
            # print(rating)
            # print(movieName)
            # print(url)
        newDict["position"]=position
        position+=1
        list1.append(newDict.copy())
    with open("task1.json","w+") as movie_data:
        json.dump(list1,movie_data,indent=4)
    return list1
        # print(list1)
        # print(newDict)
movie=scrape_top_list()
#https://www.imdb.com/title/tt0048473/