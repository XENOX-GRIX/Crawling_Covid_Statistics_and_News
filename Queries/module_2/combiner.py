import sys 

country = None 
date = None 
cases = 0 
date1 = sys.argv[1]
date2 = sys.argv[2]

for line in sys.stdin: 
    Date , Country , Cases = line.strip().split()
    try :
        Cases  = int(Cases)
    except : 
        print("Error as the space seperated strings cannot be treated as Integers")
        continue
    if str(Date) == str(date1) or str(Date) == str(date2):
        print(Date, Country, Cases)
 