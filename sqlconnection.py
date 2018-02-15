# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:02:46 2018

@author: bmart
"""

from sqlalchemy import *
from timedate import timedate
from node import Node
from host import Host

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
        self.gen_node_table()
        self.gen_host_table()

    # Simple re-creation of engine
    def reset(self):
        self._sql_engine = create_engine(self._sql_path)

    # Getters and Setters
    def get_engine(self):
        return _sql_engine


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
            to_insert = self.node_table.insert().values(ipAddr = node_ip, inUse = node_inUse, disabled = node_disabled, lastConnect = node_lastConn)
            result = self.execute(to_insert)
            return result
        else:
            print("Not a node")
            
    def add_host(self, host):
        if type(host) is Host:
            host_name = host.get_name()
            host_owner = "MANAGER"
            host_lastConn = host.host_lastConn
            host_spotCount = host.host_spotCount
            host_spotLimit = host.host_spotLimit
            to_insert = self.node_table.insert().values(hostname = host_name, owner = host_owner, lastConnect = host_lastConn, spotCount = host_spotCount, spotLimit = host_spotLimit)
            result = self.execute(to_insert)
            return result
        else:
            print("Not a host")
            
    def set_node_status(self, node):
        if type(node) is Node:
            node_ip = node.get_ip()
            node_lastConn = timedate.now()
            node_inUse = node.get_inUse()
            to_update = update(node_table).where(node_table.c.ipAddr == node_ip).values(inUse = node_inUse, lastConnect = node_lastConn)
            result = self.execute(to_update)
            return result
        else:
            print("Not a node")

    def get_all_nodes(self):
        result = self.execute("SELECT * FROM Nodes;")
        all_nodes = []
        for row in result:
            node = Node(row['id'], row['ipAddr'])
            node.set_inUse = row['inUse']
            node.set_last_connection = row['lastConnect']
            all_nodes.append(node)

        if all_nodes == []: return None
        else: return all_nodes


    """ The SQL Controller contains the structures of all tables
    involved. Re-run any table creation functions after making changes to this
    section.
    Add any other tables in a similar manner.
    """

    def gen_node_table(self):
         # Provides a python object of our Node table
         self.node_table = Table('Nodes', self._metadata,
              Column('id', Integer, primary_key=True),
              Column('ipAddr', String(15), primary_key=True),
              Column('inUse', Boolean),
              Column('disabled', Boolean),
              Column('lastConnect', DATETIME)
         )

    def gen_host_table(self):
        # Provides a python object of our Host table
        self.host_table = Table('Hosts', self._metadata,
            Column('id', Integer, primary_key=True),
            Column('hostname', String(60)),
            Column('owner', String(60)), # Will be a foreign key
            Column('lastConnect', DATETIME),
            Column('spotCount', Integer),
            Column('spotLimit', Integer),
            Column('open', Boolean)
        )

"""
Will be used later...

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
"""