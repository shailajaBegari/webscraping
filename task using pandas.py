import pandas as pd
import json
import requests
from bs4 import BeautifulSoup


url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
resp=requests.get(url).content
# print(resp)


# soup=BeautifulSoup(resp,"html.parser")
# titles=soup.find_all("td", class_="titleColumn")
# # print(titles)
# # Rating
# rating=soup.find_all("strong")
# # print(rating)

# # Images
# image=soup.find_all("img")
# # print(image)


# moveititle=[]
# moveirating=[]
# moveiyear=[]
# moveiimage=[]
# moveilink=[]
# for l in titles:
#     l1=l.a
#     l2=l1.get("href")
#     l3="https://www.imdb.com"+l2+"?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=177WBP729TB5VG0CJQ13&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_ss_toprated_tt_1"
#     moveilink.append(l3)
# # print(moveilink)

# for img in image:
#     imgs=img.get("src")
#     moveiimage.append(imgs)
# # print(moveiimage)
# for tit in titles:
#     t= tit.a.text
#     moveititle.append(t)
#     year=tit.span.text
#     moveiyear.append(year)
# for i in rating:
#     rate=i.text.strip()
#     moveirating.append(rate)


# data={"titiles":moveititle,"links":moveilink,"images":moveiimage,"ratings":moveirating,"year":moveiyear}
# df=pd.DataFrame(data=data)
# d=json.dumps(data)
# load=json.loads(d)

# with open("moveis.json","w") as f:
    # f.write(d)
























