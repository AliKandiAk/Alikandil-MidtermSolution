import validators as v #https://snyk.io/blog/secure-python-url-validation/
tab_list = [{"title": "Youtube", "url": "http://example.com/Youtube"}]

def addTab(tab_list,title,url):#choice 1 append a new dictionary to the list
    is_Url=v.url(url)# gives true if its a url or false if not 
    if is_Url:
      new_tab= {"title":title,"url":"https://www."+url+".com"}
      tab_list.append(new_tab)
      print(tab_list)
    else :
        print("incorrect url")
def Close_Tab(tab_list,index=None): # choice 2 delete tab
    if index==None:
        del tab_list[-1] # index pointing top last index in a list and deleting it  
        print("last tab has been closed")
        print(tab_list)
    else: 
        del tab_list[index] # delit dictionary acording to index
        print(tab_list)
