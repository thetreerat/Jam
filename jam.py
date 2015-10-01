import sys, psycopg2
from datetime import datetime, date
 
def opendatabase(c):
    badtrycount=0
    while True:
        try:
            badtrycount = badtrycount + 1
            p = input("Password: ") 
            c = psycopg2.connect(database='Jam', user='postgres', password=p) 
        except psycopg2.Error as e:
            if not e.pgcode:
                print("Bad password")
            else:
                print(e)
                print(e.pgcode)
                print(e.pgerror)
                sys.exit(1)

        if c:
            break
        else:
            if badtrycount>=3:
                print("Who you?")
                break
    return c

def getdatepart(msgText, p):
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
       
def mainscreenmessage():
    m = """     Main Screen
                   GET - Input Batch data
                   LOAD - Load Data into database
                   EXIT - Quit"""
    return m

def getdate(msgText, N=None, d="09", m="09", y="2015"):
   while True:
     try: 
       print(msgText)
       y = int(getdatepart('Please Enter Year [{0}] :'.format(y), y))
       m = int(getdatepart('Please Enter Month [{0}] :'.format(m), m))
       d = int(getdatepart('Please Enter Day [{0}] :'.format(d), d))
       return date(y,m,d)
     except ValueError:
       print('Not a valid date! please try again')
     except:
       print("Unexpected error")
       raise

def getbatchdata(b):
    b['mcode'] = getstring("Please enter 2 letter Batch Code: ",U=True, S='a')
    b['batchnumber'] = getnumber("Please a batch number: ", 1)
    b['jars8'] = getnumber("Enter number of 8oz Jars in Batch: ")
    b['jars4'] = getnumber("Enter number of 4oz Jars in Batch: ")
    b['jars12'] = getnumber("Enter number of 12oz Jars in Batch: ")
    b['insertdate'] = datetime.now()
    b['batchdate'] = getdate("Please enter the date the Batch was Made: ")
    return b

def getstring(msgText, Length=2, U=False, S=None):
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

def insertsql(b, con):
    try:
        if b['mcode']==None:
            print('No data entered')
            return False
        cur = con.cursor()
        cur.execute("""INSERT INTO jam_2015."BatchList" ("MCode",
                                                "BatchNumber",
                                                "Jars_8oz",
                                                "Jars_4oz",
                                                "Jars_12oz",
                                                "Batch_date",
                                                "Date_inserted")
                           VALUES (%(mcode)s,
                                   %(batchnumber)s,
                                   %(jars8)s,
                                   %(jars4)s,
                                   %(jars12)s,
                                   %(batchdate)s,
                                   %(insertdate)s);""",b)
        print('{} rows inserted '.format(cur.rowcount))
        con.commit()
        return True
    except psycopg2.DatabaseError as e:
        if e.pgcode=='23505':
            print("""Batch Code %s already used with %s Bacth Number""" % (b['mcode'],b['batchnumber']))
            return False
        
def getnumber(msgText, N=0):
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
         
if __name__ == '__main__':
    con = None
    batch = {}
    try:
        con = opendatabase(con)
        print("Hello, Database Open")
        answer = None
        while True:
            print(mainscreenmessage())
            answer = input('Now What?').upper()
            if answer in ['LOAD', 'LOA', 'LO', 'L']:
                print('Loading Data in to database ...')
                status = insertsql(batch, con)
                if status==True:
                    print('Row Added')
                else:
                    print('No Data Add to Database, Please correct error')
                input('<enter>')
            elif answer in ['GET', 'GE', 'G']:
                print('Getting Data from you ...')
                batch = getbatchdata(batch)
                #print(batch)
                input('<enter>')
            elif answer in ['EXIT', 'E', 'Q', 'QUIT']:
                break
            else:
                print('What??')
                input('<enter>')
            
    finally:
        if con:
            print("Closing Database ...")
            con.close()         
    print("bye, bye")
