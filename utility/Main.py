'''
created by: Ashis Sahoo

this module contains the function which
accepts the user's choice
'''

from ChoiceUtility import save_data

def start_project():
    choice_type = None
    choice_format = None
    
    while (True):
        print 'Choose an option from below :'
        print '1. To get new stories'
        print '2. To get top stories'
        
        choice = raw_input()
        
        if ( choice == '1'):
            choice_type = 'new'
            break
            
        elif ( choice == '2' ):
            choice_type = 'top'
            break
            
        else:
            print 'Choose a valid option'
            
    while (True):
        print 'Choose an option from below :'
        print '1. To store data in CSV'
        print '2. To store data in Sqlite'
        
        choice = raw_input()
        
        if ( choice == '1'):
            choice_format = 'CSV'
            break
            
        elif ( choice == '2' ):
            choice_format = 'Sqlite'
            break
            
        else:
            print 'Choose a valid option'
            
            
    save_data(choice_type, choice_format)
    print '{} stories saved successfully in {}'.format(choice_type.capitalize(),choice_format)
    
    return None

if __name__ == '__main__':
    start_project()