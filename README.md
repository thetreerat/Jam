# Jam
This is a sample app for job interveiw
it collects data from user and dose some simple vatation and inserts into the PostgreSQL tables.

The script uses a cisco style input. if "a" is unique that all that need to add. it dose not have an auto complete
though. 

to work:
   access to localhost PostgresSQL server running 9.4
   created database jam
   created schema jam_2015
   python 3.4
   psycopg2 install in python
   
You do no need to run createtables.py in SQL folder. (pasted into sql query tool in pgadmin III tool)
becuase there is no foreign key constrain you do not have to run  LoadMasterTable.py


run jam.py to enter batch data and load into batchlist table

