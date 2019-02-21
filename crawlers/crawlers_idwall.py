# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:32:57 2019

@author: Pedro Augusto
"""

import requests
from bs4 import BeautifulSoup

def request(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    source = requests.get('https://old.reddit.com/r/' + url + '/', headers=headers)
    return source

#%% Wrapper
if __name__ == "__main__":    
    input_ = input("Entre com os subreddits separados por ponto-e-vírgula: ")
    url = input_.split(';')
    #url = ['askreddit', 'worldnews', 'cats']
    
    for u in url:
        source = request(u)
        soup = BeautifulSoup(source.text, 'html.parser')
        
#%% Navegação pelas tags  
        subreddit = '/r/' + u
        upvotes, title, link, comments_link = [],[],[],[]
        
        for paragraph in soup.find_all('div', class_='score unvoted'):
            if paragraph.string != "•":
                upvotes.append(paragraph.get('title'))
            else:
                upvotes.append('0')
            
        for paragraph in soup.find_all('a', class_='title'):
            title.append(str(paragraph.text))
            if paragraph.get('href')[0] == '/':
                link.append('https://old.reddit.com' + paragraph.get('href'))
            else:
                link.append(paragraph.get('href'))
        
        for url in soup.find_all('a', class_={'bylink comments empty may-blank', 'bylink comments may-blank'}):
            comments_link.append(url.get('href'))
            
        if len(upvotes) == 0:
            print("Subreddit não encontrado: {0}".format(subreddit))
            continue
            
        # Remove a thread referente à propagando, caso exista    
        if len(comments_link) != len(link):
            upvotes.pop(0)
            title.pop(0)
            link.pop(0)

#%% Desconsiderar as threads com menos de 5000 upvotes            
        i, k = 0, 0
        j = len(upvotes)        
        while k < j:
            if int(upvotes[i]) < 5000:
                upvotes.pop(i)
                title.pop(i)
                link.pop(i)
                comments_link.pop(i)
            else:
               i = i + 1 
            k = k + 1    
            
        if len(upvotes) == 0:
            print("Nenhuma thread relevante para o subreddit: {0}".format(u))
            
#%% Impressão das informações
        for i in range(0, len(upvotes)): 
            print("Subreddit: {0}".format(subreddit))
            print("Título da thread: {0}".format(title[i]))
            print("Número de upvotes: {0}".format(upvotes[i]))        
            print("Link para os comentários da thread: {0}".format(comments_link[i]))
            print("Link da thread: {0}\n".format(link[i]))
            
        print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")