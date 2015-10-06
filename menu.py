import sys, os

def collecttablename():
    print(""" collecttablename""")
    return None
def mainscreenmessage():
 
    print("""     Main screen
     ---- ------
     ADD  - Input Data for Load
     LIST - List a Table
     LOAD - Load Entered Data into Table
     EXIT - Quit or Exit program""")
     
    
if __name__ == '__main__':
    try:
        while True:
            mainscreenmessage()
            answer = input('Please enter a command: ').upper()
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
                            input('List Master Codes <enter>')
                            break
                        elif answer[1] in ['BATCH', 'BATC', 'BAT', 'BA', 'B']:
                            input('List Batch Data <enter>')
                        else:
                            input('No Table Name matching input <enter>')
                    else:
                        tablename
                    
                elif answer[0] in ['LOAD', 'LOA', 'LO']:
                    if len(answer)>=2:
                        if answer[1] in ['MASTER', 'MASTE', 'MAST', 'MAS', 'MA', 'M']:
                            input('Load Master Codes <enter>')
                            break
                        elif answer[1] in ['BATCH', 'BATC', 'BAT', 'BA', 'B']:
                            input('Load Batch Data <enter>')
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
                            input('Add Master Codes <enter>')
                            break
                        elif answer[1] in ['BATCH', 'BATC', 'BAT', 'BA', 'B']:
                            input(' Add Batch Data <enter>')
                            break
                        else:
                            input('No Table Name matching <enter>')
                    else:
                        input('No Table Name Entered <enter>')
                    
                else:
                    input('Input not Valid <enter>')
                    break
    except AttributeError as e:
        print(e)
    finally:
        print("bye, bye")
