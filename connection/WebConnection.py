'''
created by: Ashis Sahoo

This module contains the classes
used to connect with Web page
'''

import urllib2


'''
this class is used to fetch 
content of a web page
'''
class WebConnect:
    def __init__(self,url):
        self.__url = url

    def get_url(self):
        return self.__url


    def set_url(self, value):
        self.__url = value
    
    
    '''
    used to get web page as response
    using request url
    :retun: Content of web page in form of string
    '''    
    def getWebContent(self):
        request = urllib2.Request(self.get_url())
        response = urllib2.urlopen(request)
        return response.read()
    
    
    
'''
To perform self test on module uncomment 
below block of code and run the module
'''
'''
if __name__ == '__main__':
    web_connect = WebConnect(url='https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty')
    page_data = web_connect.getWebContent()    
    print type(page_data)
    print page_data
    
    web_connect = WebConnect("https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format('19319890'))
    page_data = web_connect.getWebContent()    
    print type(page_data)
    print page_data
'''