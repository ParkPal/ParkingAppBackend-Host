""" This file represesnts the primary running of the program. It
is mainly a loop that monitors a group of nodes and relays the
data to a host server. """

from networking import *
from host import *
from node import *

# Defines the main funtion
def main():
    """ Both network objects will listen on different interfaces """

    """ For recieveing data from nodes """
    mesh_recieve = MeshConnection("127.0.0.1", 12345)
    mesh_recieve.init_conn()

    """ For sending data to the server """
    net_send = WebConnection("127.0.0.1", 1235)

    mesh_recieve.req_update(1)
    net_send.check_in()

    mesh_recieve.listen()   # Listens on the mesh network for data

    # A loop for the constantly running service    """
    while True:
        net_send.check_in
        if mesh_recieve.listen():
            # Logic for recieving a node packet
        elif net_send

        print("Monitoring...")

    # Flow:
    #   - listen on mesh port.
    #   - recieve data from node
    #   - store nodes data OR add the node
    #   - transmit data to server

# Run the program
main()
