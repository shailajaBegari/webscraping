import json
import requests
from bs4 import BeautifulSoup
# from task1 import scrape_top_movies

movieurl='https://www.rottentomatoes.com/m/toy_story_4'
moviename='toy_story_4'


def scrape_top_movies(movieurl):
    request=requests.get(movieurl)
    soup=BeautifulSoup(request.text,'html.parser')
    
    
    maindiv=soup.find_all('li',class_='meta-row clearfix')
    for v in maindiv:
        x=v.get_text().strip()
        y=x.split()
        print(y)
        


        
        

            

scrape_top_movies(movieurl)