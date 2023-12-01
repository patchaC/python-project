# install gazpacho
!pip install gazpacho
import gazpacho

# start webscraping # HTTP request

import pandas as pd
import requests
from gazpacho import Soup

url = "https://www.imdb.com/search/title/?sort=user_rating,desc&groups=top_100"

html = requests.get(url,
                    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'})

imdb = Soup(html.text)
imdb

# find 'titles'
titles = imdb.find("h3", {"class": "ipc-title__text"})
titles = [title.strip() for title in titles]
titles.pop(50)
clean_titles = [title.split(".")[1] for title in titles]
clean_titles

# find 'ratings'
ratings = imdb.find("div", {"class":"sc-e3e7b191-0 jlKVfJ sc-479faa3c-2 eUIqbq dli-ratings-container"})
ratings = [rating.strip() for rating in ratings]
clean_ratings = [rating.split("(")[0] for rating in ratings]
clean_ratings

#find 'years'
years = imdb.find("span", {"class": "sc-479faa3c-8 bNrEFi dli-title-metadata-item"})
years = [year.strip() for year in years]
years = [year.split(',')[0] for year in years]
clean_years = years[::3]
clean_years

# create new dataframe
df = pd.DataFrame( data =
    {
        "title" : clean_titles,
        "release_year" : clean_years,
        "rating" : clean_ratings
        
    }
)
df
