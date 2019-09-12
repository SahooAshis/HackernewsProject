'''
created by: Ashis Sahoo

This module contains the classes
which represent the tables of sqlite
database

'''

class Story:
    
    row_schema = {'id':'NA', 'by':'NA', 'time':'NA', 'type':'NA',
                   'title':'NA', 'url':'NA', 'text':'NA',
                    'score':'NA','descendants':'NA', 'kids':'NA'}
    
    def __init__(self, params=row_schema):
        self.__by = params['by']
        self.__descendants = params['descendants']
        self.__id = params['id']
        self.__score = params['score']
        self.__time = params['time']
        self.__title = params['title']
        self.__type = params['type']
        self.__url = params['url']
        self.__text = params['text']
        self.__kids = params['kids']

    def get_text(self):
        return self.__text


    def get_kids(self):
        return self.__kids


    def set_text(self, value):
        self.__text = value


    def set_kids(self, value):
        self.__kids = value


    def del_text(self):
        del self.__text


    def del_kids(self):
        del self.__kids


    def get_by(self):
        return self.__by


    def get_descendants(self):
        return self.__descendants


    def get_id(self):
        return self.__id


    def get_score(self):
        return self.__score


    def get_time(self):
        return self.__time


    def get_title(self):
        return self.__title


    def get_type(self):
        return self.__type


    def get_url(self):
        return self.__url


    def set_by(self, value):
        self.__by = value


    def set_descendants(self, value):
        self.__descendants = value


    def set_id(self, value):
        self.__id = value


    def set_score(self, value):
        self.__score = value


    def set_time(self, value):
        self.__time = value


    def set_title(self, value):
        self.__title = value


    def set_type(self, value):
        self.__type = value


    def set_url(self, value):
        self.__url = value


    def del_by(self):
        del self.__by


    def del_descendants(self):
        del self.__descendants


    def del_id(self):
        del self.__id


    def del_score(self):
        del self.__score


    def del_time(self):
        del self.__time


    def del_title(self):
        del self.__title


    def del_type(self):
        del self.__type


    def del_url(self):
        del self.__url
        
        
    '''
    this method return the string 
    representation of the object of class
    :return: string
    '''
    def __str__(self):
        rows = [str(self.get_id()),
                '"'+ self.get_by() + '"',
                str(self.get_time()),
                '"'+ self.get_type() + '"',
                '"'+ self.get_title() + '"',
                '"'+ self.get_url() + '"',
                '"'+ self.get_text() + '"',
                str(self.get_score()),
                str(self.get_descendants()),
                '"'+ self.get_by() + '"'
                ]
        return '(' +",".join(rows) + ')'



    