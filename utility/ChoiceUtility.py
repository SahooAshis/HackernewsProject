'''
created by: Ashis Sahoo

this module contains the function which
controls the flow of the project as per
user request
'''

from functionality.HackerNewsCSV import HackerNewsCSV
from functionality.HackerNewsSqlite import HackerNewsSqlite


'''
This method is used to save
data either in .csv or sqlite database
as per user's choice
'''
def save_data(choice_type, choice_format): 
    
    if ( choice_format == 'CSV'):
        obj = HackerNewsCSV(choice_type)
        print "Saving the {} stories in CSV file...Please waits...Do not terminate the program.".format(choice_type)
        obj.save_data()
        
    else:
        obj = HackerNewsSqlite(choice_type)
        print "Saving the {} stories in database...Please wait...Do not terminate the program.".format(choice_type)
        obj.save_data()
    