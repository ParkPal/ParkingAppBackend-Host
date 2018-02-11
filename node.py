"""
This class defines an object that represents a single parking space node.
The host node software will maintain a list of these objects to allow it
to track its child nodes.
"""

from timedate import timedate

class Node:    
    """ Variables """
    node_id = None          # Identification number of the node
    node_ipAddr = None      # IP Address of the node
    node_lastConn = None    # String representing time of last connection
    node_inUse = None      # Boolean value representing if the spot is taken
    node_disabled = None

    """ Initialization """
    def __init__(self, id, ipAddr):
        self.node_id = id
        self.node_ipAddr = ipAddr
        self.node_inUse = False
        self.node_disabled = False
        self.node_lastConn = timedate.now()
        print("New node object created...")

    """ Member Functions """
    def get_info(self):
        return "ID: " + str(self.node_id) + " | IP: " + str(self.node_ipAddr) + " | Status: " + str(self.node_status)

    """ Getters and Setters """        
    def get_id(self):
        return self.node_id
    def set_id(self, id):
        self.node_id = id
        
    def get_ip(self):
        return self.node_ipAddr
    def set_ip(self, ip):
        self.node_ipAddr = ip
        
    def get_last_connection(self):
        return self.node_lastConn
    def set_last_connection(self, time):
        self.node_lastConn = time
        
    def get_inUse(self):
        return self.node_inUse
    def set_inUse(self, status):
        self.node_inUse = status
        
    def get_disabled(self):
        return self.node_disabled
    def set_disabled(self, disabled):
        self.node_disabled = disabled