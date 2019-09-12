'''
created by: Ashis Sahoo

This module contains the classes
used to connect with Sqlite Database
'''


import sqlite3 as sql
from models.StoryClass import Story

'''
below class is used to connect ,
create table and insert data
row-wise into a table
'''

class DBConnector:
    
    def __init__(self, db):
        self.__db = db

    def get_db(self):
        return self.__db

    def set_db(self, value):
        self.__db = value
        

    '''create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    '''
    def create_connection(self):
        try:
            conn = sql.connect(self.get_db())
            return conn
        except Exception as e:
            print(e)    
        return None
    
    
    """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
    """
    def create_table_story(self,conn,choice_type):
        try:            
            cur = conn.cursor()
            drop_table_sql = 'DROP TABLE IF EXISTS {}stories;'.format(choice_type)
            cur.execute(drop_table_sql)
            create_table_sql = '''
                                CREATE TABLE IF NOT EXISTS {}stories (
                                id integer PRIMARY KEY,
                                by text,
                                time integer,
                                type text,
                                title text,
                                url text,
                                text text,
                                score integer,
                                descendants integer,
                                kids text
                                );
                                '''.format(choice_type)
            cur.execute(create_table_sql)
        except Exception as e:
            print(e)
        
    
    """ insert a row to specified table using 
        :insert_sql: query to be executed
        :return: None
    """        
    def inset_row_story(self,con,choice_type,row_values):
        try:
            story = Story(row_values)
            cur = con.cursor()
            insert_sql = "INSERT INTO {}stories VALUES {};".format(choice_type, str(story))
            cur.execute(insert_sql)
            con.commit()
        except Exception as e:
            print e
        
        
    '''
    close the sqlite database connection
        :return: None
    '''
    def close_connection(self,con):
        con.close()
         

'''
To perform self test on module uncomment 
below block of code and run the module
'''

'''if __name__ == "__main__":
    obj = DBConnector('../files/database.db')
    con = obj.create_connection()
    cur = con.cursor()
    data = cur.execute('select * from newstories')
    for i in data:
        print i
    con.close()'''
    
    
