"""
This is the code that will simulate the host for our first demo.
It will wait for a message from the node then broadcast it to
the server.
"""

from networking import MeshConnection, WebConnection
from sqlconnection import SQLController
from host import Host
from node import Node
import socket

def main():
    """ Create an object that represents this lot. """
    this_lot = Host("Summit Hall Lot")
    this_lot.set_id(1)

    """ Creates a way of interacting with the local sql database """
    sql_controller = SQLController("mysql://manager:password@localhost/host_db")

    """ Creates a way of broadcasting messages to the server """
    server_connection = WebConnection("65.183.143.248", 12345)
    server_connection.init_conn()

    while True:
        """ Wait for object to be sent from a node """
        mesh_connection = MeshConnection("192.168.2.1", 12345)
        mesh_connection.init_conn()
        obj = mesh_connection.listen()

        """ Relay data to the server """
        if type(obj) is Node:
            sql_controller.set_node_status(obj)
            this_lot.add_node(obj)
            server_connection.transmit_object(this_lot)
            print("Node recieved and data sent...")
            mesh_connection.close_conn()

    else:
        print("Recieved garbage from node")

main()
