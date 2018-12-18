#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 14:34:47 2018

@author: ekinsilahlioglu,selinyesilselve,kadirakgul
"""

# Fetching data(commments) from Eksisozluk using Beautiful Soup
import requests
from bs4 import BeautifulSoup as bsoup

website = 'https://eksisozluk.com/'
header = {'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML_like Gecko) Chrome/39.0.2171.95 Safari/537.36'} #we wrote this to avoid eskisozluk's bot
firstTopic = []
secondTopic = []

#Eksisozluk topics
topic = 'elon musk'
topic2 = 'iphone'
    
r = requests.get(website + topic, headers = header) #we create our url
site = r.url
pageNo = "?p=" #this adjusts the page number, you see this string when you look at the url part of any site.
count = 1
site = site + pageNo + str(count)

#same steps for our second topic
r2 = requests.get(website + topic2, headers = header)
site2 = r2.url
count2 = 1
site2 = site2 + pageNo + str(count2)
    
    
if(r.status_code != 200):
    print('Can not find the page! Try Again.') 
else:
    while r.status_code == 200 : #status code == 200 means if there is something on the page status code will be 200.
        site = site[:site.index("=")+1] + str(count)
        newPage = requests.get(site, headers = header)
        soup = bsoup(newPage.content, 'html.parser')
        
        
        #it finds the comments in the html code section(comments are exist between entry-item-list section)
        if soup.find(id='entry-item-list'):
            entries = soup.find('ul', id = 'entry-item-list').find_all('li')
            for entry in entries:
                content = entry.find(class_ = 'content').get_text(strip = True) #it takes the content of the entry-item-list which is our comments
                print(content)
                firstTopic.append(content)
            if count == 60: #it takes the comment until page number 60.
                break
            count = count + 1
                   
    
if(r2.status_code != 200):
    print('Can not find the page! Try Again.') 
else:
    while r2.status_code == 200 :
        site2 = site2[:site2.index("=")+1] + str(count2)
        newPage2 = requests.get(site2, headers = header)
        soup2 = bsoup(newPage2.content, 'html.parser')
        
        
        #it finds the comments in the html code section(comments are exist between entry-item-list section)
        if soup2.find(id='entry-item-list'):
            entries2 = soup2.find('ul', id = 'entry-item-list').find_all('li')
            for entry in entries2:
                content2 = entry.find(class_ = 'content').get_text(strip = True)#it takes the content of the entry-item-list which is our comments
                print(content2)
                secondTopic.append(content2)
            if count2 == 90: #it takes the comment until page number 90.
                break
            count2 = count2 + 1



AllTopic = firstTopic + secondTopic #we gather all two topics' comments into one array

            

import csv
wtr = csv.writer(open ('Comments.csv', 'w'), delimiter=',', lineterminator='\n') #we write our array into csv file later on to be labelled
for x in AllTopic : wtr.writerow ([x])


