import sys, os

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
            a = tuple(answer.split())
            if a[0] in ['EXIT', 'EXI', 'EX', 'E', 'QUIT', 'QUI', 'QU', 'Q']:
                break
            elif a[0] in ['HAL']:
                os.system('cls')
                print("He is a good guy")
                input('<enter>')
                os.system('cls')            
            elif a[0] in ['LIST', 'LIS', 'LI']:
                if len(a)>=2:
                    if a[1] in ['MASTER', 'MASTE', 'MAST', 'MAS', 'MA', 'M']:
                        input('List Master Codes <enter>')
                    elif a[1] in ['BATCH', 'BATC', 'BAT', 'BA', 'B']:
                        input('List Batch Data <enter>')
                    else:
                        input('No Table Name matching input <enter>')
                else:
                    input('No Table Name Entered <enter>')

            elif a[0] in ['LOAD', 'LOA', 'LO']:
                if len(a)>=2:
                    if a[1] in ['MASTER', 'MASTE', 'MAST', 'MAS', 'MA', 'M']:
                        input('Load Master Codes <enter>')
                    elif a[1] in ['BATCH', 'BATC', 'BAT', 'BA', 'B']:
                        input('Load Batch Data <enter>')
                    else:
                        input('No Table Name matching <enter>')
                else:
                    input('No Table Name Entered <enter>')

            elif a[0] in ['ADD', 'AD', 'A']:
                if len(a)>=2:
                    if a[1] in ['MASTER', 'MASTE', 'MAST', 'MAS', 'MA', 'M']:
                        input('Add Master Codes <enter>')
                    elif a[1] in ['BATCH', 'BATC', 'BAT', 'BA', 'B']:
                        input(' Add Batch Data <enter>')
                    else:
                        input('No Table Name matching <enter>')
                else:
                    input('No Table Name Entered <enter>')
                    
            else:
                input('Input not Valid <enter>')
    finally:
        print("bye, bye")
