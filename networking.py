"""This class defines an object that can be instantiated
in order to create a connection to one or multiple
management servers. Essentially server client code.

Packages Used:

"""

import socket
import pickle

from host import Host
from node import Node

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

    def close_conn(self):
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()

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
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.conn_hostname, self.conn_port))

    def listen(self):
        print("Listening")
        self.s.listen()

        connection, client_addr = self.s.accept()

        obj = self.recieve_object(connection)

        if type(obj) is Host:
                tmp = "Host: " + obj.get_name()
        elif type(obj) is Node:
                tmp = "Node: " + obj.get_info()
        else:
                tmp = "No Data"
                print("None")
        print("Connection! Recieved data... | " + tmp)

        connection.close()
        return obj

    def recieve_object(self, conn):
        final = conn.recv(1024)
        obj = pickle.loads(final)
        return obj

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
        data = pickle.dumps(data)
        self.s.sendall(data)
