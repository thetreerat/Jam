# Jam
This is a sample app for job interveiw
it collects data from user and dose some simple vatation and inserts into the PostgreSQL tables.

to work:
   access to localhost PostgresSQL server running 9.4
   created database jam
   created schema jam_2015
   python 3.4
   psycopg2 install in python
   
you need to run createtables.py in SQL folder (pasted into sql query tool in pgadmin III tool)
becuase there is no foreign key constrain you do not have to run  LoadMasterTable.py but in furture you will
run jam.py

