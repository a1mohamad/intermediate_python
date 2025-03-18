import requests
import re
from bs4 import BeautifulSoup
def agreement_func(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_objects = soup.find_all('div', attrs= {'class': 'kt-post-card__body'})
    result = ''
    for one_object in all_objects:
        agreement_founder = one_object.find_all('div', attrs= {'class': 'kt-post-card__description'})
        for every in agreement_founder:
            if re.search(r'توافقی', every.text) != None:
                result += f'({one_object.h2.text}) در ({one_object.span.text})\n'
    return print(result)
agreement_func('http://divar.ir/s/tehran') #this is my local first page of Divar
#we can promote our app with input.use this just by removing hashtag:
#url1 = input('insert your divar url: ')
#agreement_func(url1)