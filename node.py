"""
This class defines an object that represents a single parking space node.
The host node software will maintain a list of these objects to allow it
to track its child nodes.
"""

class Node:    
    """ Variables """
    node_id = None          # Identification number of the node
    node_ipAddr = None      # IP Address of the node
    node_lastConn = None    # String representing time of last connection
    node_status = None      # Boolean value representing if the spot is taken

    """ Initialization """
    def __init__(self, id, ipAddr):
        self.node_id = id
        self.node_ipAddr = ipAddr
        self.node_status = False
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
        
    def get_status(self):
        return self.node_status
    def set_status(self, status):
        self.node_status = status