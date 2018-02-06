# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:02:46 2018

@author: bmart
"""

from sqlalchemy import *

class SQLController:

    _sql_engine = None
    _sql_path = None
    
    def __init__(self, path):
        self._sql_path = path
        self._sql_engine = create_engine(self._sql_path)
     
    def reset(self):
        self._sql_engine = create_engine(self._sql_path)
        
    def get_engine(self):
        return _sql_engine;
    
    
    """ The SQL Controller contains the structures of all tables
    involved. Re-run any table creation functions after making changes to this
    section """
    
    def get_node_table(self, metadata):
        # Provides a python object of our Node table
        node_table = Table('Nodes', metadata,
            Column('id', Integer, primary_key=True),
            Column('inUse', Boolean),
            Column('disabled', Boolean),
            Column('lastConnect', DATETIME)
       )
        return node_table
    
    def get_host_table(self, metadata):
        # Provides a python object of our Host table
        host_table = Table('Hosts', metadata,
            Column('id', Integer, primary_key=True),
            Column('hostname', String(60)),
            Column('owner', String(60)), # Will be a foreign key
            Column('lastConnect', DATETIME),
            Column('spotCount', Integer),
            Column('spotLimit', Integer),
            Column('open', Boolean)
        )
        return host_table
    
    def get_user_table(self, metadata):
        # Provides a python object of our User Table
        user_table = Table('Users', metadata,
            Column('id', Integer, primary_key=True),
            Column('username', String(60)),
            Column('lastLogin', DATETIME)
        )
        return user_table
    
    def get_report_table(self, metadata):
        # Provides a python object of our User Table
        user_table = Table('Users', metadata)
        return user_table