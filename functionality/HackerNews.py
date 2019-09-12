'''
created by: Ashis Sahoo

This module contains the abstract classes

'''


from abc import ABCMeta, abstractmethod
from StoryFetch import get_story_details, get_story_ids

'''
abstact class which provides the prototype
for data fetch and save in desired format
'''
class HackerNews:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def save_data(self):
        pass

    
    '''
    This method is used to fetch story IDs
    from the API Web Page
    '''  
    def fetch_story_ids(self):
        return get_story_ids(self.get_choice_type())
    
    
    '''
    This method is used to fetch the details 
    of a specific story ID
    '''    
    def fetch_story_details(self,story_id):
        return get_story_details(story_id)      
    
    
    