from datetime import datetime, date

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
       print(msgText) y = int(GetDatePart('Please Enter Year [{0}] :
       '.format(y), y)) m = int(GetDatePart('Please Enter Month [{0}] :
       '.format(m), m)) d = int(GetDatePart('Please Enter Day [{0}] :
       '.format(d), d)) TheDate = date(y,m,d) return TheDate break
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

if __name__ == '__main__': 
    MCode = Getstring("Please enter 2 letter Batch Code: ",U=True, S='a')
    BatchNumber = GetNumber("Please a batch number: ", 1)
    Jars8 = GetNumber("Enter number of 8oz Jars in Batch: ")
    Jars4 = GetNumber("Enter number of 4oz Jars in Batch: ")
    Jars12 = GetNumber("Enter number of 12oz Jars in Batch: ")
    InsertDate = datetime.now()
    InsertDate2 = datetime.utcnow()
    BatchDate = GetDate("Please enter the date the Batch was Made: ")
    print("")
    print("Master Batch Code: " + MCode)
    print("Batch Number: " + str(BatchNumber))
    print("Full Batch Code: " + MCode + str(BatchNumber))
    print("Number of 8oz Jars: " + str(Jars8))
    print("Number of 4oz Jars: " + str(Jars4))
    print("Number of 12oz Jars: " + str(Jars12))
    print("Date Batch Made: " + str(BatchDate))
    print ("Date recorded in Database: " + str(InsertDate) + " " + str(InsertDate.tzname()))
    print ("Date recorded in Database: " + str(InsertDate2) + " " + str(InsertDate.tzname()))
