# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:36:19 2019

@author: Pedro Augusto
"""

from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup
import logging

def request(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    source = requests.get('https://old.reddit.com/r/' + url + '/', headers=headers)
    return source

def NadaPraFazer(bot, update, args):
    msg = "Subreddit CRAWLER [Idwall]:\n\n"
    bot.send_message(chat_id=update.message.chat_id, text=msg) 
    
    url = args[0].split(';')
    
    for u in url:
        msg = "\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n" 
        source = request(u)
        soup = BeautifulSoup(source.text, 'html.parser')
        
        #Navegação pelas tags  
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

        # Desconsiderar as threads com menos de 5000 upvotes            
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
            bot.send_message(chat_id=update.message.chat_id, text="Nenhuma thread relevante para o subreddit: {0}".format(u))
            
        # Impressão das informações
        for i in range(0, len(upvotes)): 
            msg += "Subreddit: {0}\n".format(subreddit)
            msg += "Título da thread: {0}\n".format(title[i])
            msg += "Número de upvotes: {0}\n".format(upvotes[i])   
            msg += "Link para os comentários da thread: {0}\n".format(comments_link[i])
            msg += "Link da thread: {0}\n\n".format(link[i])
            
            bot.send_message(chat_id=update.message.chat_id, text=msg)
            msg = ''
            
        del msg    
            
def start(bot, update):
    me = bot.get_me()
    
    msg = "Hello!\n"
    msg += "I'm {0} and I came here to help you to get reddit data.\n".format(me.first_name)
    msg += "Click /NadaPraFazer to start the crawler, it will wait for you to pass all subreddits that you want (separated each one by semicolon (;)) \n\n"

    bot.send_message(chat_id=update.message.chat_id, text=msg)

if __name__ == "__main__":   
    updater = Updater(token='768765479:AAFAOG6qA5gZzAIduOCI4OOak5Q_sfOA7dc')
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(CommandHandler('NadaPraFazer', NadaPraFazer, pass_args=True))
    updater.start_polling()
    updater.idle()



