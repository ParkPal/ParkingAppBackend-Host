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
    def print_info(self):
        print("ID: " + str(self.node_id) + " | IP: " + str(self.node_ipAddr) + " | Status: " + str(self.node_status))