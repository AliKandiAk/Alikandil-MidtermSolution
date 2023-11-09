tab_list = [
    {"title": "Youtube", "url": "http://example.com/Youtube"},
    {"title": "GitHub", "url": "http://example.com/GitHub"},
    {"title": "Replit", "url": "http://example.com/Replit"}
]


def addTab(tab_list,title,url):#choice 1 append a new dictionary to the list
    new_tab= {"title":title,"url":url}
    tab_list.appemt(new_tab)

def Close_Tab(tab_list,index=None): # choice 2 delete tab
    if index==None:
        del tab_list[-1] # index pointing top last index in a list and deleting it  
        print("last tab has been closed")
        print(tab_list)
    else: 
        del tab_list[index] # delit dictionary acording to index
        print(tab_list)
