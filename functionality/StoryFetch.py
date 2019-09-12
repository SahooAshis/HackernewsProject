'''
created by: Ashis Sahoo

This module contains the methos
which get input from connections classes 
and return the output in a desired formt

'''

from connection.WebConnection import WebConnect
from ast import literal_eval


'''
this method fetch the story_ids from
APIs and returns in the form of list
:return: List<str>
'''
def get_story_ids(choice_type):
    web_connect = WebConnect('https://hacker-news.firebaseio.com/v0/{}stories.json?print=pretty'.format(choice_type))
    web_data = web_connect.getWebContent()
    story_ids = web_data[1:len(web_data)-1].strip(']').strip(' ').split(", ")
    return story_ids


'''
this method fetch the story_id details
Aand returns in the form of dictionary
:return: dict object
'''
def get_story_details(story_id):
    story_details = {'id':story_id, 'by':'NA', 'time':'NA', 'type':'NA',
                      'title':'NA', 'url':'NA', 'text':'NA', 'score':'NA',
                      'descendants':'NA', 'kids':'NA'}
    web_connect = WebConnect("https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(story_id))
    web_data = web_connect.getWebContent()
    if web_data != 'null\n':
        story_details.update(literal_eval(web_data))
        return story_details
    else:
        return story_details
    
    

'''
To perform self test on module uncomment 
below block of code and run the module
'''
'''       
if __name__ == '__main__':
    
    var1 = get_story_ids('top')
    print type(var1)
    print (var1)
    
    var2 =  get_story_details('19326397')
    print type(var2)
    print var2
''' 
