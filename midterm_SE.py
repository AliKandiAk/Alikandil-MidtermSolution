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
