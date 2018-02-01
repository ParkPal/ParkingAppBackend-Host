"""
This class defines an object that can be instantiated
in order to create a connection to one or multiple
management servers. Essentially server client code.

Packages Used:

"""

import socket
import time
import pickle

from host import *

class NetworkConnection:
    """Variables that are used to maintain connection """
    s = None
    conn_hostname = ""
    conn_port = ""

    """Initialization"""
    def __init__(self, url, port):
        self.s = socket.socket()
        self.conn_hostname = url
        self.conn_port = port

        print("New networking class created...")
        print("Using Path: " + self.gen_path())


    """ Member Functions """
    def gen_path(self):
        return self.conn_hostname + ":" + str(self.conn_port)

    def lib_check(self):
        print("Library is imported...")

    """ Getters and Setters """
    def get_url(self):
        return self.conn_hostname

    def set_url(self, url):
        self.conn_hostname = url

    def get_port(self):
        return self.conn_port

    def set_port(self, port):
        self.conn_port = port
        
class MeshConnection(NetworkConnection):
    def init_conn(self):
        self.s.bind((self.conn_hostname, self.conn_port))

    def listen(self):
        print("Listening")
        self.s.listen()
        while True:
            connection, client_addr = self.s.accept()
            data = connection.recv(1024)
            host_obj = pickle.loads(data)
            print("connection made, received: " + host_obj.get_name())

        # Clean up the connection
        connection.close()
            
    def req_update(self, node):
        # Ask a node for an update
        print("Requesting...")
    
class WebConnection(NetworkConnection):
    def init_conn(self):
        self.s.connect((self.conn_hostname, self.conn_port))

    def check_in(self):
        print("Checking in with host")
        
    def req_new_lot_id(self):
        """ Asks server for next available host id """
        print("Function not yet implemented...")
        return 0
    
    def register_lot(self, host):
        """ Transmits host object to the server. """
        print("Function not yet implemented...")
        return False
    
    def transmit_bytes(self, data):
        """ Transmits the given byte object """
        self.s.sendall(data)
        
    def transmit_object(self, data):
        """ Will pickle the given object and transmit it. """
        self.s.sendall(data)