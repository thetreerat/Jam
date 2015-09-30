from datetime import datetime, date
import sys
import psycopg2

def InsertSQL(B):
   con = None 
   try:
      p = input("Password: ") 
      con = psycopg2.connect(database='Jam', user='postgres', password=p) 
      cur = con.cursor()
      cur.execute("""INSERT INTO jam_2015."BatchList" ("MCode",
                                                     "BatchNumber",
                                                     "Jars_8oz",
                                                     "Jars_4oz",
                                                     "Jars_12oz",
                                                     "Batch_date",
                                                     "Date_inserted")
                     VALUES (%(MCode)s,
                             %(BatchNumber)s,
                             %(Jars8)s,
                             %(Jars4)s,
                             %(Jars12)s,
                             %(BatchDate)s,
                             %(InsertDate)s);""",B)
      print(cur.statusmessage)
      print('{} rows inserted '.format(cur.rowcount))
      con.commit()
    

   except psycopg2.DatabaseError as e:
      print (e)   
      sys.exit(1)
    
    
   finally:
    
      if con:
         con.close()
   

def GetDatePart(msgText, p):
   while True:
     try:
       DatePart = input(msgText)
       #print('datepart: {}'.format(DatePart))
       if DatePart:
         p = DatePart
       #print('p: {}'.format(p))
       return p
     except:
       print("Unexpected error")

def GetDate(msgText, N=None, d="09", m="09", y="2015"):
   while True:
     try: 
       print(msgText)
       y = int(GetDatePart('Please Enter Year [{0}] :'.format(y), y))
       m = int(GetDatePart('Please Enter Month [{0}] :'.format(m), m))
       d = int(GetDatePart('Please Enter Day [{0}] :'.format(d), d))
       return date(y,m,d)
       break
     except ValueError:
       print('Not a valid date! please try again')
     except:
       print("Unexpected error")
       raise


def Getstring(msgText, Length=2, U=False, S=None):
   while True:
     try:
        if S:
          msgText = '{0} [{1}] '.format(msgText, S)
        MCode = input(msgText)
        #see if defualt, is so set
        if not MCode:
           MCode = S
        #test for length   
        if len(MCode) <= Length:
           if U:
              MCode = MCode.upper()
           return MCode
        else:
           #repeat for proper lenth
           raise Exception('TooLong')
     except Exception as e:
        #print(e)
        print("Code to long. Try agian...")

def GetNumber(msgText, N=0):
   while True:
      try:
         TheNumber = input(msgText + "[" + str(N) + "] ")
         if not TheNumber:
           TheNumber = int(N)
         else:
             TheNumber = int(TheNumber)
         return TheNumber
         break
      except ValueError:
         print("That was not a valid number.  Try again...")

def PrintResults(B):
    print("")
    print("Master Batch Code: " + Batch['MCode'])
    print("Batch Number: " + str(Batch['BatchNumber']))
    print("Full Batch Code: " + Batch['MCode'] + str(Batch['BatchNumber']))
    print("Number of 8oz Jars: " + str(Batch['Jars8']))
    print("Number of 4oz Jars: " + str(Batch['Jars4']))
    print("Number of 12oz Jars: " + str(Batch['Jars12']))
    print("Date Batch Made: " + str(Batch['BatchDate']))
    print ("Date recorded in Database: " + str(Batch['InsertDate']) + " " + str(Batch['InsertDate'].tzname()))
    print ("Date recorded in Database: " + str(Batch['InsertDate2']) + " " + str(Batch['InsertDate'].tzname()))
   
if __name__ == '__main__':
    Batch = {}
    Batch['MCode'] = Getstring("Please enter 2 letter Batch Code: ",U=True, S='a')
    Batch['BatchNumber'] = GetNumber("Please a batch number: ", 1)
    Batch['Jars8'] = GetNumber("Enter number of 8oz Jars in Batch: ")
    Batch['Jars4'] = GetNumber("Enter number of 4oz Jars in Batch: ")
    Batch['Jars12'] = GetNumber("Enter number of 12oz Jars in Batch: ")
    Batch['InsertDate'] = datetime.now()
    Batch['InsertDate2'] = datetime.utcnow()
    Batch['BatchDate'] = GetDate("Please enter the date the Batch was Made: ")
    InsertSQL(Batch)
    #PrintResults(Batch)
