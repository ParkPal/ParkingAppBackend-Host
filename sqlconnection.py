# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:02:46 2018

@author: bmart
"""

from sqlalchemy import *
from node import Node

class SQLController:

    # Lets use getters and setter, feels safer....
    _sql_engine = None
    _sql_path = None
    
    _metadata = None
    
    node_table = None
    host_table = None
    
    # Initial creation of the controller. One for an instance.
    def __init__(self, path):
        self._sql_path = path
        self._sql_engine = create_engine(self._sql_path)
        self._metadata = MetaData()
        self.node_table = self.get_node_table()
     
    # Simple re-creation of engine
    def reset(self):
        self._sql_engine = create_engine(self._sql_path)
        
    # Getters and Setters
    def get_engine(self):
        return _sql_engine;
    
    
    # Member Functions
    
    """ Executes a generic query and returns the result """
    def execute(self, query):
        result = self._sql_engine.execute(query)
        return result
    
    def add_node(self, node):
        if type(node) is Node:
            node_ip = node.get_ip()
            node_lastConn = node.get_last_connection()
            node_inUse = node.get_inUse()
            node_disabled = node.get_disabled()
            to_insert = self.node_table.insert().values(ipAddr = node_ip, ipinUse = node_inUse, disabled = node_disabled, lastConnect = node_lastConn)
            result = self.execute(to_insert)
            return result
        else:
            print("Not a node")
        
    

    
    """ The SQL Controller contains the structures of all tables
    involved. Re-run any table creation functions after making changes to this
    section.
    Add any other tables in a similar manner.
    """
    
    def get_node_table(self):
        # Provides a python object of our Node table
        node_table = Table('Nodes', self._metadata,
            Column('id', Integer, primary_key=True),
            Column('ipAddr', String),
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
        user_table = Table('Reports', metadata)
        return user_table