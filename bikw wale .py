from typing import Text
import requests
from bs4 import BeautifulSoup
import csv
url="https://www.bikewale.com/royalenfield-bikes/"
page=requests.get(url)
# print(page)

soup=BeautifulSoup(page.content,"html.parser")
print(soup.prettify())
# print(soup.text)

# image
img1=[]
image=soup.findAll("div",class_="imageWrapper")
# print(image)
# for i in image:
    # j=i.img["src"]
    # print(j)
    # img1.append(j)
# print(img1)

# links

links=[]
link=soup.findAll("div", class_="bikeDescWrapper")
# print(link)
for i in link:
    j=i.a["href"]
    links.append(j)
# print(links)


# Text
links=[]
link=soup.findAll("div", class_="bikeDescWrapper")
# print(link)
for i in link:
    j=i.a.text
    links.append(j)
# print(links)

# using csv  we have to store the data:
with open("file.csv","w") as csv_file:
    write=csv.writer(csv_file)
    write.writerow(image)
    for i in image:
        j=i.img["src"]
        img1.append(j)
    write.writerow(img1)

