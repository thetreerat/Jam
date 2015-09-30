import sys
import psycopg2

def InsertSQL(B, con):
   try:
      cur = con.cursor()
      cur.execute("""INSERT INTO jam_2015."MasterBatchCodes" ("MCode",
                                                     "JamName")
                     VALUES (%(MCode)s,
                             %(JamName)s);""",B)

      print('{} rows inserted '.format(cur.rowcount))
      con.commit()
    

   except psycopg2.DatabaseError as e:
      print (e)   
      return


def LoadData():
    print("Loading list with Data ...")
    Codes = []
    Code = {'MCode': 'A', 'JamName': 'Raspberry'}
    Codes.append(Code)
    Code = {'MCode': 'B', 'JamName': 'Blueberry'}
    Codes.append(Code)
    Code = {'MCode': 'C', 'JamName': 'Red Current'}
    Codes.append(Code)
    Code = {'MCode': 'D', 'JamName': 'Black Raspberry'}
    Codes.append(Code)
    Code = {'MCode': 'E', 'JamName': 'Gooseberry'}
    Codes.append(Code)
    Code = {'MCode': 'F', 'JamName': 'Blueberry-Apricot'}
    Codes.append(Code)
    Code = {'MCode': 'G', 'JamName': 'Strawberry-Ginger'}
    Codes.append(Code)
    Codes.reverse()
    return Codes
    print ("Data Load in to list")
    
def WarrningMessage():
    print("""

This is a one time script for loading MCodes in to MasterBatchCodes



""")

if __name__ == '__main__':
    WarrningMessage()
    Answer = input("Do you still want to Run(yes)? ")
    if Answer.upper()=='YES':
      CodeList = LoadData()
      con = None
      try:
        p = input("Password: ") 
        con = psycopg2.connect(database='Jam', user='postgres', password=p) 

        while len(CodeList):
          # need to clean up so not open and closing connection 
          InsertSQL(CodeList.pop(), con)  
      except psycopg2.DatabaseError as e:
        print (e)   
        sys.exit(1)
    
    
      finally:
    
        if con:
           con.close()         
          
    #print(CodeList)
