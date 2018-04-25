# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:02:46 2018
@author: bmart
"""

from sqlalchemy import *
from datetime import datetime
from host import Host
from node import Node

class SQLController:

    # Lets use getters and setter, feels safer....
    _sql_engine = None
    _sql_path = None

    _metadata = None

    node_table = None
    host_table = None
    user_table = None

    # Initial creation of the controller. One for an instance.
    def __init__(self, path):
        self._sql_path = path
        self._sql_engine = create_engine(self._sql_path)
        self._metadata = MetaData()
        self.gen_node_table()
        self.gen_host_table()
        self.gen_user_table()

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
            host_owner = 1
            host_lastConn = datetime.now()
            to_insert = self.node_table.insert().values(hostname = host_name, owner = host_owner, lastConnect = host_lastConn)
            result = self.execute(to_insert)
            return result
        else:
            print("Not a host")


    def set_host_status(self, host):
        if type(host) is Host:
            host_lastConn = datetime.now()
            host_curCap = self.get_host_cap(host)
            host_spotCount = len(host.get_nodes())
            host_inUse = self.get_host_in_use(host) 
            to_update = update(self.host_table).where(self.host_table.c.lotName == host.get_name()).values( currentCapacity = host_curCap, lastConnect = host_lastConn, spotCount = host_spotCount, spotlimit = host_inUse)
            result = self.execute(to_update)
            return result
        else:
            print("Not a host!")
            
    def get_host_in_use(self, host):
        x = 0
        if len(host.get_nodes()) > 0:
            for node in host.get_nodes():
                if node.get_inUse() == True:
                    x += 1
                    print(host.get_name()+" ")
                    print(x)
                    print(node.get_inUse())
            return x
        else:
            print("No nodes!")
            return 0
        
    def get_host_cap(self, host):
        x = 0
        if len(host.get_nodes()) > 0:
            for node in host.get_nodes():
                if node.get_inUse() == False:
                    x += 1
                    print(host.get_name()+ " ")
                    print(x)
                    print(node.get_inUse())
            return (x/len(host.get_nodes()))*100.00
        else:
            print("Host has no nodes!")
            return 0
        
            
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
         self.node_table = Table('polls_node', self._metadata,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('ipAddr', String(15), primary_key=True),
                                 Column('host_id', Integer, ForeignKey("polls_host.id")),
              Column('inUse', Boolean),
              Column('disabled', Boolean),
              Column('lastConnect', DATETIME)
         )

    def gen_host_table(self):
        # Provides a python object of our Host table
        self.host_table = Table('polls_host', self._metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('lotName', String(200)),
            Column('hostname', String(60)),
            Column('owner', Integer, ForeignKey("auth_user.id")), # Will be a foreign key
            Column('lastConnect', DATETIME),
            Column('spotCount', Integer),
            Column('spotlimit', Integer),
            Column('open', Boolean),
            Column('currentCapacity', Numeric(3,2))
                                
        )


    def gen_user_table(self):
        # Provides a python object of our User Table
        self.user_table = Table('auth_user', self._metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('password', String(128)),
            Column('username', String(150), unique = True),
            Column('last_login', DATETIME),
            Column('is_superuser', Boolean),
            Column('first_name', String(30)),
            Column('last_name', String(150)),
            Column('email', String(254)),
            Column('is_staff', Boolean),
            Column('is_active', Boolean),
            Column('date_joined', DATETIME)
        )
"""    
    def get_report_table(self, metadata):
        # Provides a python object of our User Table
        user_table = Table('Reports', metadata)
        return user_table
"""