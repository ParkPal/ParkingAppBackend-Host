from sqlconnection import SQLController
from sqlalchemy import MetaData

"""
This file is used for the initial creation of tables required
for the primary program to operate. Incorporation into main
is tbd.
"""


# Defines the main funtion
def create_tables():
    sql_controller = SQLController("mysql://USERNAME:PASSWORD@localhost:PORT/DBNAME")
    
    metadata = MetaData();

    # Calls for each table object. Comment out any you don't wish to create
    node_table = sql_controller.get_node_table(metadata)
    host_table = sql_controller.get_host_table(metadata)
    user_table = sql_controller.get_user_table(metadata)
    report_table = sql_controller.get_report_table(metadata)
    
    # Execute Creation
    metadata.create_all(sql_controller._sql_engine)
    
# Run the program
create_tables()