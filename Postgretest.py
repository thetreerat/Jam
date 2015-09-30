import sys
import psycopg2

def StringBuilder(Batch=[]):
   try:
      s = """{MCode}""".format(Batch)
         
      return s
   except:
      print('Error: {0}'.format(e))
      
con = None

try:
    p = input("Password: ") 
    con = psycopg2.connect(database='Jam', user='postgres', password=p) 
    cur = con.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print(ver)   
    
    print(StringBuilder())    

except psycopg2.DatabaseError as e:
    print (e)   
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()

        
