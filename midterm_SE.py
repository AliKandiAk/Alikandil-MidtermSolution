import validators as v #https://snyk.io/blog/secure-python-url-validation/
import requests
import json
from bs4 import BeautifulSoup 
tab_list = [
    {
        "title": "Youtube",
        "url": "https://www.youtube.com/",
        "nested_tabs": [
            {"title": "Subtab 1", "url": "http://example.com/Subtab1"}
        ]
    },
    {
        "title": "Google",
        "url": "https://www.google.com/",
        "nested_tabs": [
            {"title": "Subtab 2", "url": "http://example.com/Subtab2"},
            {"title": "Subtab 3", "url": "http://example.com/Subtab3"}
        ]
    },
    {
        "title": "Facebook",
        "url": "https://www.facebook.com/",
        "nested_tabs": [
            {"title": "Subtab 4", "url": "http://example.com/Subtab4"},
            {"title": "Subtab 5", "url": "http://example.com/Subtab5"}
        ]
    }
    # Add more tabs as needed
]
def addTab(tab_list,title,url):#choice 1 append a new dictionary to the list
    is_Url=v.url(url)# gives true if its a url or false if not 
    if is_Url:
      new_tab= {"title":title,"url":"https://www."+url+".com"}
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

def Open_nestedTab(tab_list, nested_tab, index):  # choice 5
    if 0 <= index < len(tab_list): # check for open tabs 
        if 'nested_tabs' not in tab_list[index]: # if a tab has no nesdted tasb 
            tab_list[index]['nested_tabs'] = []  # create an empty list for the tab that doesn't have nested tabs
        tab_list[index]['nested_tabs'].append(nested_tab)  # append the new nested tab
        print(f"Nested tab has beeen added to '{tab_list[index]['title']}' at the index {index}.")
    else:
        print(f"Invalid index: {index}")

def display_Tabs(tab_list, depth=0):#choice 4 
    for tab in tab_list:
        print(" - " * depth + f"{tab['title']}")  # print the title of the main tab

        if 'nested_tabs' in tab:
            display_Tabs(tab['nested_tabs'], depth + 1)  # recursively display nested tabs with increased depth


def clear_Tabs(tablist):#choice 6 
   tab_list.clear() # cleared all the tabs that are open
   print("tabs have been cleard")

def SaveTabs(tab_list, filepath):#choice 7 
    with open(filepath, 'w') as jsonfile: # open file to write for it 
        
        json_data = json.dumps(tab_list) # convert to json formated string using .dumps
        
        # Write the JSON-formatted string to the file
        jsonfile.write(json_data) # writing to the file the formated string 
      
def checkjson(file):
  pass
file='file.json'


def Import_Tabs(file):#choice 8 #https://github.com/nkmk/python-snippets/blob/5ad4cd3391ffdd8bf9d16d46d110db0fe3e9eced/notebook/json_example.py#L21-L28
    with open(file) as f:
      d = json.load(f)
    print(d)
  
Import_Tabs(file)
