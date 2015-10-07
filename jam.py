import sys, psycopg2
from datetime import datetime, date

def addbatchdata(batch):
    print('Getting Data from you ...')
    batch['mcode'] = getstring("Please enter 2 letter Batch Code: ",U=True, S='a')
    batch['batchnumber'] = getnumber("Please a batch number: ", 1)
    batch['jars8'] = getnumber("Enter number of 8oz Jars in Batch: ")
    batch['jars4'] = getnumber("Enter number of 4oz Jars in Batch: ")
    batch['jars12'] = getnumber("Enter number of 12oz Jars in Batch: ")
    batch['insertdate'] = datetime.now()
    batch['batchdate'] = getdate("Please enter the date the Batch was Made: ")
    input('<enter>')
    return batch


def getdate(msgtext, N=None, d="09", m="09", y="2015"):
   while True:
     try: 
       print(msgtext)
       y = int(getdatepart('Please Enter Year [{0}] :'.format(y), y))
       m = int(getdatepart('Please Enter Month [{0}] :'.format(m), m))
       d = int(getdatepart('Please Enter Day [{0}] :'.format(d), d))
       return date(y,m,d)
     except ValueError:
       print('Not a valid date! please try again')
     except:
       print("Unexpected error")
       raise
 
def getdatepart(msgtext, p):
   while True:
     try:
       DatePart = input(msgtext)
       #print('datepart: {}'.format(DatePart))
       if DatePart:
         p = DatePart
       #print('p: {}'.format(p))
       return p
     except:
       print("Unexpected error")

def addmastercode(mastercode):
    print('Getting master code data from you')
    mastercode['mcode'] = getstring("Please enter 2 letter Batch Code: ", Length=2, U=True, S=None)
    mastercode['jamname'] = getstring("Please Enter Jam Name", Length=32, U=False, S=None)
    input('<enter>')
    return mastercode

def getnumber(msgtext, N=0):
   while True:
      try:
         TheNumber = input(msgtext + "[" + str(N) + "] ")
         if not TheNumber:
           TheNumber = int(N)
         else:
             TheNumber = int(TheNumber)
         return TheNumber
         break
      except ValueError:
         print("That was not a valid number.  Try again...")

def getstring(msgtext, Length=2, U=False, S=None):
   while True:
     try:
        mcode = None
        defualttext = ""
        #see if defualt value is set 
        if S:
            defualttext = '[{1}] '.format(defualttext, S)
            if not mcode:
                mcode = S
        #Ask for mcode
        mcode = input('{0} {1}'.format(msgtext, defualttext))
        
        #test for length   
        if len(mcode) <= Length:
           if U:
              mcode = mcode.upper()
           return mcode
        else:
           #repeat for proper lenth
           raise Exceptioneption('TooLong')
     except Exception as e:
        print(e)
        #print("Code to long. Try agian...")
        sys.exit(1)

def insertmasterbatcodes(mastercode, con, c):
    try:
        if 'mcode' in mastercode:
            cur = con.cursor()
            cur.execute("""select * from jam_2015."MasterBatchCodes"
                           where "MCode" = %(mcode)s""",mastercode)
            if not cur.rowcount:
                cur.execute("""INSERT INTO jam_2015."MasterBatchCodes" ("MCode",
                                                     "JamName")
                               VALUES (%(mcode)s,
                                       %(jamname)s);""",mastercode)

                c += 1
                con.commit()
                return c
            else:
                print("Master Code in Database")
        else:    
            return False

    except psycopg2.DatabaseError as e:
      print (e)   
      return

def insertsql(b, con):
    try:
        if not 'mcode' in b:
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
        cur.close()
        return True
    except psycopg2.DatabaseError as e:
        if e.pgcode=='23505':
            print("""Batch Code %s already used with %s Bacth Number""" % (b['mcode'],b['batchnumber']))
            return False
def listbatchdata(con):
    try:
        print('Batch Data')
        print('----- ----')
        cur = con.cursor()
        cur.execute("""SELECT 
  "MasterBatchCodes"."JamName", 
  "BatchList"."MCode", 
  "BatchList"."BatchNumber", 
  "BatchList"."Jars_8oz", 
  "BatchList"."Jars_4oz", 
  "BatchList"."Jars_12oz", 
  "BatchList"."Batch_date", 
  "BatchList"."Date_inserted"
FROM 
  jam_2015."BatchList", 
  jam_2015."MasterBatchCodes"
WHERE 
  "BatchList"."MCode" = "MasterBatchCodes"."MCode"
ORDER BY
  "BatchList"."MCode" ASC, 
  "BatchList"."BatchNumber" ASC;
 """)
        row = cur.fetchone()
        print("""Batch  Jam                                               Batch      Insert
Code   Name                                 4oz 8oz 12oz Date       Date
----   ---------------------------------    --- --- ---- ---------  ---------------------""")
        while row:
            mc = ("""%s%s""" % (row[1].strip(), row[2])).ljust(5)
            print("""%s   %s  %s %s %s  %s %s""" % (mc, row[0].ljust(34), str(row[2]).ljust(3), str(row[3]).ljust(3), str(row[5]).ljust(3), row[6], row[7]))
            row = cur.fetchone()
        print("{} row(s)".format(cur.rowcount))
        input('<enter>')
        return codes
    finally:
        cur.close()
def listmastercodes(con):
    codes = []
    try:
        print('Master Codes List')
        print ('------ ----- ---- ')
        cur = con.cursor()
        cur.execute("""SELECT * FROM jam_2015."MasterBatchCodes" ORDER BY "MasterBatchCodes"."MCode" ASC;  """)
        row = cur.fetchone()
        print("""Master Jam
Code   Name
----   ---------------------------------""")
        while row:
            print("""%s     %s""" % (row[0],row[1]))
            row = cur.fetchone()
        print("{} row(s)".format(cur.rowcount))
        input('<enter>')
        return codes
    except psycopg2.Error as e:
        print(e)
        input('<enter>')
        return False
    finally:
        cur.close()
        
def loadbatchdata(batch, con):
    print('Loading Data in to database ...')
    status = insertsql(batch, con)
    if status==True:
        print('Row Added')
    else:
        print('No Data Add to Database, Please correct error')
    input('<enter>')

def loadmastercode(mastercode, con):
    RowCount = 0
    print('Add New Master Code')
    status = insertmasterbatcodes(mastercode, con, RowCount)
    if status:
        print('{0} Row(s) added'.format(status))
    else:
        print('No Records added')
    input('<enter>')
    
        
def mainscreenmessage():
    m = """     Main screen
     ---- ------
     ADD  - Input Data for Load
     LIST - List a Table
     LOAD - Load Entered Data into Table
     EXIT - Quit or Exit program"""
    return m


def opendatabase(c):
    badtrycount=0
    while True:
        try:
            badtrycount += 1
            p = input("Password: ")
            if p:
                c = psycopg2.connect(database='Jam', user='postgres', password=p)
            else:
                print('No Password entered, Bye, Bye')
                sys.exit(1)
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
                print("Could not open Database, Bye, Bye!")
                sys.exit(1)
    return c
   
         
if __name__ == '__main__':
    con = None
    batch = {}
    mastercode = {}
    codes = []
    try:
        con = opendatabase(con)
        print("Hello, Database Open")
        answer = None
        while True:
            print(mainscreenmessage())
            answer = input('Now What?').upper()
            answer = list(answer.split())
            while answer:
                if answer[0] in ['EXIT', 'EXI', 'EX', 'E', 'QUIT', 'QUI', 'QU', 'Q']:
                    sys.exit(1)
                elif answer[0] in ['HAL']:
                    os.system('cls')
                    print("He is a good guy")
                    input('<enter>')
                    os.system('cls')            
                elif answer[0] in ['LIST', 'LIS', 'LI']:
                    if len(answer)>=2:
                        if answer[1] in ['MASTER', 'MASTE', 'MAST', 'MAS', 'MA', 'M']:
                            codes = listmastercodes(con)
                            break
                        elif answer[1] in ['BATCH', 'BATC', 'BAT', 'BA', 'B']:
                            b = listbatchdata(con)
                            break
                        elif answer[1] in ['EXIT', 'EXI', 'EX', 'E']:
                            break
                        elif answer[1] in ['QUIT', 'QUI', 'QU', 'Q']:
                            sys.exit(1)
                        else:
                            answer[1] = input('Invalid table name, please reenter MASTER OR BATCH :').upper()
                    else:
                        answer.append(input('No Table Name Entered, Please pick MASTER or BATCH :').upper())                    
                elif answer[0] in ['LOAD', 'LOA', 'LO']:
                    if len(answer)>=2:
                        if answer[1] in ['MASTER', 'MASTE', 'MAST', 'MAS', 'MA', 'M']:
                            loadmastercode(mastercode, con)
                            break
                        elif answer[1] in ['BATCH', 'BATC', 'BAT', 'BA', 'B']:
                            loadbatchdata(batch, con)
                            break
                        elif answer[1] in ['EXIT', 'EXI', 'EX', 'E']:
                            break
                        elif answer[1] in ['QUIT', 'QUI', 'QU', 'Q']:
                            sys.exit(1)
                        else:
                            answer[1] = input('Invalid table name, please reenter MASTER OR BATCH :').upper()
                    else:
                        answer.append(input('No Table Name Entered, Please pick MASTER or BATCH :').upper())    
                elif answer[0] in ['ADD', 'AD', 'A']:
                    if len(answer)>=2:
                        if answer[1] in ['MASTER', 'MASTE', 'MAST', 'MAS', 'MA', 'M']:
                            mastercode = addmastercode(mastercode)
                            break
                        elif answer[1] in ['BATCH', 'BATC', 'BAT', 'BA', 'B']:
                            batch = addbatchdata(batch)
                            break
                        elif answer[1] in ['EXIT', 'EXI', 'EX', 'E']:
                            break
                        elif answer[1] in ['QUIT', 'QUI', 'QU', 'Q']:
                            sys.exit(1)
                        else:
                            answer[1] = input('Invalid table name, please reenter MASTER OR BATCH :').upper()
                    else:
                        answer.append(input('No Table Name Entered, Please pick MASTER or BATCH :').upper())                    
                else:
                    input('Input not Valid <enter>')
                    break
    except AttributeError as e:
        print(e)
                    
    finally:
        if con:
            print("Closing Database ...")
            con.close()         
    print("bye, bye")
