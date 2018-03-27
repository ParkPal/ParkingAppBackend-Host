"""
This class defines an object that represents a single parking lot host.
A host node will instantiate one instance of this per geographical lot it
manages (usually 1).

1. Send request to server for next available Lot ID
2. Create new Host object (give it unused name0 with this ID.
3. Pickle Host Object and Transmit to Server.

"""

from node import Node

class Host:
    """ Variables """
    host_id = None      # This value is provided by the server.
    host_name = None    # This string is given TO the server
    
    host_nodes = None   # This is a list of node objects that represent spots
                        # Nodes are added as they connect for the first time
    
    """ Initialization """
    def __init__(self, name):
        self.host_name = name
        self.host_nodes = []
        print("New Empty Parking Lot Created...")
    
    """ Member Functions """
    def add_node(self, node):
        if type(node) is Node:
            self.host_nodes.append(node)
        else:
            print("Object not a node...")
    
    """ Getters and Setters """
    def set_id(self, id):
        self.host_id = id
    def get_id(self):
        return self.host_id
    
    def set_name(self, name):
        self.host_name = name
    def get_name(self):
        return self.host_name
    
    def get_nodes(self):
        return self.host_nodes