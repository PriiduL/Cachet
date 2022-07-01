import sqlite3
from sqlite3 import Error
import os

class SQLite3_run:
    '''For this class we need sqlite file and data for queries'''
    def __init__(self, sqlite3_file, sqlite3_data):
        self.sqlite3_file = sqlite3_file
        self.sqlite3_data = sqlite3_data
    
    def create(self):
        '''Create connection to data base'''
        try:
            self.sqlite3_connect = sqlite3.connect(self.sqlite3_file)
        except Error as error:
            print("Error: ", error)

    def connect(self):
        '''Connect to data base, if sqlite file exists'''
        if os.path.exists(self.sqlite3_file) and os.path.isfile(self.sqlite3_file):
            self.create()
        else:
            print(f'Database file "{self.sqlite3_file}" is not exist')

    def execute(self):
        '''Execute the query.
            Optinally: fetch data in case of SELECT query
        '''
        if hasattr(self, 'sqlite3_connect'):
            try:
                cursor = self.sqlite3_connect.cursor()
                cursor.execute(self.sqlite3_data)
                rows = cursor.fetchall()
                self.sqlite3_connect.commit()
                # cursor.close()                
                return rows
            except Error as error:
                self.sqlite3_connect.rollback()
                print(f'SQL error: {error}')

    def disconnect(self):
        '''Disconnect and close connection to data base'''
        if hasattr(self, 'sqlite3_connect'):
            self.sqlite3_connect.close

def sqlite3_create(sqlite3_file, sqlite3_data):
    sqlite3_create = SQLite3_run(sqlite3_file, sqlite3_data)
    sqlite3_create.create()
    sqlite3_create.execute()
    sqlite3_create.disconnect()

def sqlite3_run(sqlite3_file, sqlite3_data):
    sqlite3_run = SQLite3_run(sqlite3_file, sqlite3_data)
    sqlite3_run.connect()
    fetch = sqlite3_run.execute()
    sqlite3_run.disconnect()

    return fetch
