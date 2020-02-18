import requests
from bs4 import BeautifulSoup
import pandas as pd

sirealNumber=[]
movieName=[]
movieYear=[]
movieGenre=[]
movieRating=[]

URL="https://www.imdb.com/list/ls041322734/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

#find divs whose class=lister list detail sub-list
table = soup.find('div', attrs = {'class':'lister list detail sub-list'})

#find all spans whose class=lister-item-index unbold text-primary
for sno in table.findAll('span', attrs={'class':'lister-item-index unbold text-primary'}):
    sirealNumber.append(sno.text.strip("."))

#find all h3 whose class=lister-item-header
for mName in table.findAll('h3', attrs={'class':'lister-item-header'}):
    for movieNames in mName.findAll('a'):
        movieName.append(movieNames.text)

#find all spans whose class=lister-item-year text-muted unbold
for years in table.findAll('span',attrs={'class':'lister-item-year text-muted unbold'}):
    movieYear.append(years.text.strip("()"))

#find all spans whose class=genre
for genres in table.findAll('span', attrs={'class':'genre'}):
    movieGenre.append(genres.text[1:])

#find all divs whose class=ipl-rating-star small
for ratingsTab in table.findAll('div',attrs={'class':'ipl-rating-star small'}):
    for ratings in ratingsTab.findAll('span', attrs={'class':'ipl-rating-star__rating'}):
        movieRating.append(ratings.text)

#transfer those data into panda format

dat1 = pd.DataFrame(sirealNumber)
dat1.columns = ['Serial Number']
result1A = dat1

dat2 = pd.DataFrame(result1A)
dat3 = pd.DataFrame(movieName)
dat3.columns = ['Movie Name']
result2A = dat2.join(dat3)

dat4 = pd.DataFrame(result2A)
dat5 = pd.DataFrame(movieYear)
dat5.columns = ['Movie Year']
result3A = dat4.join(dat5)

dat6 = pd.DataFrame(result3A)
dat7 = pd.DataFrame(movieGenre)
dat7.columns = ['Movie Genre']
result4A = dat6.join(dat7)

dat8 = pd.DataFrame(result4A)
dat9 = pd.DataFrame(movieRating)
dat9.columns = ['Movie Rating']
result4A = dat8.join(dat9)

#write to csv
df1 = pd.DataFrame(result4A)
df1.to_csv('movie.csv', encoding='utf-8', index=False)
