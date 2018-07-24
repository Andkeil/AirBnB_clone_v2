#!/usr/bin/python3
'''
    Testing the db_storage module.
'''

import os
import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage


class testDBStorage(unittest.TestCase):
    '''
        Testing the DBStorage class
    '''
    def setUpClass(cls):
        os.environ['HBNB_MYSQL_USER'] = 'hbnb_test'
        os.environ['HBNB_MYSQL_PWD'] = 'hbnb_test_pwd'
        os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        os.environ['HBNB_MYSQL_DB'] = 'hbnb_test_db'
        
    def setUp(self):
        '''
            Initializing tables and declaritive classes, and open session
        '''
        self.storage = DBStorage()
        self.storage.reload()
        ## insert some starter data - after testing insert capability