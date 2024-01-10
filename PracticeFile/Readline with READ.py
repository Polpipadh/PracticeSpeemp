box = open("READ.py","r")
line = box.readline()
while len(line) >  0 :
    print(line)
    line = box.readline()
box.close()
