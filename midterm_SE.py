import validators as v #https://snyk.io/blog/secure-python-url-validation/
import requests
import json
from bs4 import BeautifulSoup 

tab_list=[]
def addTab(tab_list,title,url):#choice 1 append a new dictionary to the list
    is_Url=v.url(url)# gives true if its a url or false 
    if is_Url: 
      new_tab= {"title":title,"url":url}
      tab_list.append(new_tab) # append new tab to the list 
      print("Welcome to"+title)
      print(tab_list)
    else: 
        print("incorrect url")

def Close_Tab(tab_list,index=None): # choice 2 delete tab
    if index is None:
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

def display_Tabs(tab_list, depth=0):  # choice 4 
    for tab in tab_list:
        if 'title' in tab:#check if title in tab
            print(" - " * depth + f"{tab['title']}")  # print the title of the main tab

        if 'nested_tabs' in tab: # check for nested tabs is tab
            display_Tabs(tab['nested_tabs'], depth + 1)  # recursively display nested tabs with increased depth

def Open_nestedTab(tab_list, nested_tab, index):  # choice 5
    if 0 <= index < len(tab_list): # check for open tabs 
        if 'nested_tabs' not in tab_list[index]: # if a tab has no nesdted tab 
            tab_list[index]['nested_tabs'] = []  # create an empty list for the tab that doesn't have nested tabs
        tab_list[index]['nested_tabs'].append(nested_tab)  # append the new nested tab
        print(f"Nested tab has beeen added to '{tab_list[index]['title']}' at the index {index}.")
    else:
        print(f"Invalid index: {index}")

def clear_Tabs(tablist):#choice 6 
   tablist.clear() # cleared all the tabs that are open
   print("tabs have been cleard")

def SaveTabs(tab_list, filepath):#choice 7 #https://www.datacamp.com/tutorial/json-data-python
    with open(filepath, 'w') as jsonfile: # open file to write for it 
        
        json_data = json.dumps(tab_list) # convert to json formated string using .dumps
        
        # Write the JSON-formatted string to the file
        jsonfile.write(json_data) # writing to the file the formated string 
      
def is_json(file):
  check=file.split('.') # split creats a list and put items on each index after "."
  if check[1]=='json'and len(check)==2:# check if at index 1 has word string json and the length is only 1 so only 2 indexs 0 and 1 
        return True
  else:
      return False
      
def Import_Tabs(file,tablist):#choice 8 #https://github.com/nkmk/python-snippets/blob/5ad4cd3391ffdd8bf9d16d46d110db0fe3e9eced/notebook/json_example.py#L21-L28
    d=[]
    with open(file) as f:
      d = json.load(f)# loads the data from json file to python file and print it 
      tab_list.append(d)# append the json data to the main tab list 
    print(tab_list)


while True:
      print("1. Open Tab")
      print("2. Close Tab")
      print("3. Switch Tab")
      print("4. Display All Tabs")
      print("5. Open Nested Tab")
      print("6. Clear All Tabs")
      print("7. Save Tabs ")
      print("8. Import Tabs")
      print("9. Exit")
      x=input("Enter Choice Number:")
      if x=="1":
          title=input('Enter Title:')
          Url=input("Enter Url:")
          addTab(tab_list,title,Url)
      elif x=="2":
          i= int(input("Enter tab index to close:"))
          Close_Tab(tab_list,i)
          print("tab has  been closed")
      elif x=="3":
          indx=int(input("enter index of tab to display it content:"))
          Switch_Tab(tab_list,indx)
      elif x=="4":
          display_Tabs(tab_list)
      elif x=="5":
          index1=int(input('enter index'))
          if 0<=index1 and index1<len(tab_list) :
            title1=input("enter title:")
            url1=input("Enter url:")
            if v.url(url1) ==True :
              nest={"title":title1,"url":url1}
              Open_nestedTab(tab_list,nest,index1)
            else:
                print("Not a url")
          else:
              print("Index about of bound")
          
      elif x=="6":
          clear_Tabs(tab_list)
      elif x=="7":
          file=input('enter file path')
          if is_json(file)==True:
            SaveTabs(tab_list,file)
            print("Tabs have been saved")
          else:
              print("not a json file")
      elif x=="8":
          file1=input('enter file path')
          if is_json(file1)==True:
            Import_Tabs(file1,tab_list)
          else:
              print("Not a json file")
      elif x=="9":
          exit()
      else:
          print("error Enter one of the available numbers")
