import sys 

file = open(sys.argv[3], "w")
file.write(f"News From {sys.argv[1]} to {sys.argv[2]} :\n")
date_initial = None 
sentence = ""
for line in sys.stdin: 
    date, s = line.strip().split("\t")
    if date != date_initial:
        if date_initial != None : 
            file.write(f"{date} : {sentence}\n")
            sentence = ""
    date_initial = date 
    sentence+=s
file.write(f"{date} : {sentence}\n")