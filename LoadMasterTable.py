import sys
import psycopg2

def InsertSQL(B, con, C):
   try:
      cur = con.cursor()
      cur.execute("""select * from jam_2015."MasterBatchCodes"
                     where "MCode" = %(mcode)s""",B)
      if not cur.rowcount:
         cur.execute("""INSERT INTO jam_2015."MasterBatchCodes" ("MCode",
                                                     "JamName")
                        VALUES (%(mcode)s,
                                %(jamname)s);""",B)

         C = cur.rowcount + C
      con.commit()
      return C

   except psycopg2.DatabaseError as e:
      print (e)   
      return


def loaddata():
    print("Loading list with Data ...")
    codes = []
    code = {'mcode': 'A', 'jamname': 'Raspberry'}
    codes.append(code)
    code = {'mcode': 'B', 'jamname': 'Blueberry'}
    codes.append(code)
    code = {'mcode': 'C', 'jamname': 'Red Current'}
    codes.append(code)
    code = {'mcode': 'D', 'jamname': 'Black Raspberry'}
    codes.append(code)
    code = {'mcode': 'E', 'jamname': 'Gooseberry'}
    codes.append(code)
    code = {'mcode': 'F', 'jamname': 'Blueberry-Apricot'}
    codes.append(code)
    code = {'mcode': 'G', 'jamname': 'Strawberry-Ginger'}
    codes.append(code)
    code = {'mcode': 'AA', 'jamname': 'Strawberry-Lemon'}
    codes.append(code)
    code = {'mcode': 'AB', 'jamname': 'Strawberr-Sour Cherry'}
    codes.append(code)
    code = {'mcode': 'AC', 'jamname': 'Strawberry-Raspberry-Black Raspberry'}
    codes.append(code)
    #New Lins if needed
    #code = {'mcode': '', 'jamname': ''}
    #codes.append(code)

    codes.reverse()
    return codes
    print ("Data Load in to list")
    
def warrningmessage():
    print("""

This is a one time script for loading Mcodes in to MasterBatchcodes



""")

if __name__ == '__main__':
    warrningmessage()
    answer = input("Do you still want to Run(yes)? ")
    if answer.upper()=='YES':
      currentcount = 0 
      codelist = loaddata()
      con = None
      try:
        p = input("Password: ") 
        con = psycopg2.connect(database='Jam', user='postgres', password=p) 

        for code in codelist:
          # need to clean up so not open and closing connection 
          currentcount = InsertSQL(code, con, currentcount)
          
      except psycopg2.DatabaseError as e:
        print (e)   
        sys.exit(1)
    
    
      finally:
    
        if con:
           con.close()         
      print('{}'.format(currentcount))    
    
