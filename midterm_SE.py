import validators as v #https://snyk.io/blog/secure-python-url-validation/
import requests
import json
from bs4 import BeautifulSoup
tab_list=[]
def addTab(tab_list,title,url):#choice 1 append a new dictionary to the list
    is_Url=v.url(url)# gives true if its a url or false if not 
    index=len(tab_list)
    if is_Url:
      new_tab= {"title":title,"url":url,"index":index}
      tab_list.append(new_tab)
      print("Welcome to"+title)
      print(tab_list)
    elif is_Url==False :
        print("incorrect url")

def Close_Tab(tab_list,index=None): # choice 2 delete tab
    if index==None:
        del tab_list[-1] # index pointing top last index in a list and deleting it  
        print("last tab has been closed")
        print(tab_list)
    else: 
        del tab_list[index] # delete dictionary acording to index
        print(tab_list)
        
def Switch_Tab(tab_list,index=None):# choice 3 
    if index is None:

      html_text=requests.get(tab_list[-1]["url"])#https://www.w3schools.com/python/ref_requests_get.asp
      soup=BeautifulSoup(html_text.content,'html.parser')#https://www.educative.io/answers/beautiful-soup-prettify
      print(soup.prettify())  # prittify method got from a wbsite link above 
    else :
      html_text=requests.get(tab_list[index]["url"])#https://www.w3schools.com/python/ref_requests_get.asp
      soup=BeautifulSoup(html_text.content,'html.parser')#https://www.educative.io/answers/beautiful-soup-prettify
      print(soup.prettify())  # prittify method got from a wbsite link above 
