tab_list = [
    {"title": "Youtube", "url": "http://example.com/Youtube"},
    {"title": "GitHub", "url": "http://example.com/GitHub"},
    {"title": "Replit", "url": "http://example.com/Replit"}
]


def addTab(tab_list,title,url):#choice 1 append a new dictionary to the list
    new_tab= {"title":title,"url":url}
    tab_list.appemt(new_tab)
