"""
This is the code that will simulate the host for our first demo.
It will wait for a message from the node then broadcast it to
the server.
"""

from networking import MeshConnection, WebConnection
from sqlconnection import SQLController
from host import Host
from node import Node

def main():
    """ Create an object that represents this lot. """
    this_lot = Host("new_lot")

    """ Creates a way of interacting with the local sql database """
    sql_controller = SQLController("mysql://manager:password@localhost/host_db")

    """ Creates a way of listening for messages from the node """
    mesh_connection = MeshConnection("192.168.2.1", 12345)
    mesh_connection.init_conn()

    """ Creates a way of broadcasting messages to the server """
    #server__connection = WebConnection("SERVER_IP", SERVER_PORT)

    while True:
        """ Wait for object to be sent from a node """
        obj = mesh_connection.listen()

        """ Relay data to the server """
        if type(obj) is Node:
            sql_controller.add_node(obj)
            print("Node recieved")
        else:
            print("Recieved garbage from node")
main()
