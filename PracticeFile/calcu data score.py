SUM  = 0 ; n = 3

box  = open("DATASCORE.py", "r")
for j in range(n) :
    line = box.readline()
    x = line.split()
    SUM += float(x[1])
box.close()


print(box)
print(
print("Av = ",SUM/n) 