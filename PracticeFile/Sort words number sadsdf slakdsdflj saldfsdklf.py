b = "sdkljsdjl ksdagmkssd jfj skjaskfj ksjf"
box = b.split()

gox = []

for i in range(len(box)):
    gox.append([len(box[i]), box[i]])

gox.sort()

sox = [] 
for i in range(len(gox)) :
    sox.append(gox[i][1])
    
print(sox) 
    