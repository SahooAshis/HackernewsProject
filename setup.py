'''
Created on Mar 7, 2019

@author: ASHIS SAHOO

this module is used to 
convert the project to a 
executable file
'''
from distutils.core import setup
import py2exe
  
setup(console=['run.py'])

