'''
created by: Ashis Sahoo

This module contains the classes
which interact with .csv files

'''

from HackerNews import HackerNews
from StoryFetch import get_story_details, get_story_ids
import csv


'''
This class is used to fetch web page data
and store the data in .csv file
'''
class HackerNewsCSV(HackerNews):
    
    def __init__(self,choice_type):
        self.__choice_type = choice_type

    def get_choice_type(self):
        return self.__choice_type

    def set_choice_type(self, choice_type):
        self.__choice_type = choice_type
    
    
    '''
    This function is used to save
    the fetch data in .csv file
    :return: None
    '''
    def save_data(self):        
        try:
            if self.get_choice_type() == 'top':
                csv_file = r'../files/TopStories.csv'
            else:
                csv_file = r'../files/NewStories.csv'
            csv_columns = ['id', 'by', 'time', 'type', 'title', 'url', 'text', 'score','descendants', 'kids']
            with open(csv_file, 'wb') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for story_id in self.fetch_story_ids():
                    data = self.fetch_story_details(story_id)
                    print 'Copying : {} \r'.format(data['url'][:20]+'...'),
                    print '{}\r'.format(''*35),
                    writer.writerow(data)
        except IOError as e:
            print "I/O error",e
    
    
    