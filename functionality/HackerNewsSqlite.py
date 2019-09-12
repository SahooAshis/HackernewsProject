'''
created by: Ashis Sahoo

This module is used to fetch details from 
Web Page and store them in sqlite database

'''

from HackerNews import HackerNews

from connection.DBConnection import DBConnector


'''
This class is used to store details of
story IDs in story table
'''
class HackerNewsSqlite(HackerNews):
    
    def __init__(self,choice_type):
        self.__choice_type = choice_type
        
    def get_choice_type(self):
        return self.__choice_type

    def set_choice_type(self, choice_type):
        self.__choice_type = choice_type
        
    
    '''
    This function is used to save
    the fetch data in story table 
    :return: None
    '''    
    def save_data(self):
        try:
            dbconnector = DBConnector('../files/database.db')
            conn = dbconnector.create_connection()
            dbconnector.create_table_story(conn, self.get_choice_type())
            for story_id in self.fetch_story_ids():
                data = self.fetch_story_details(story_id)
                print 'Inserting : {} \r'.format(data['url'][:20]+'...'),
                print '{}\r'.format(''*35),
                dbconnector.inset_row_story(conn,self.get_choice_type(),data)
        except Exception as e:
            print e
        finally:
            dbconnector.close_connection(conn)
                
    
        
        
    
    
