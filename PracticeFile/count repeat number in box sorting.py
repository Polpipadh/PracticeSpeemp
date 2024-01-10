data =  '123 123 423 423 42543212 121 12 231 23 4 43 1 4 33 234 2  2 2 3 4'


g = data.split()

box = [float(e) for e in g]

box.sort() 



print(box)

box.append(box[-1]+1) # tech trick  
e = box[0]
c = 1
for i in range(1,len(box)) :
    if box[i] == e :
        c +=1
    else :
        print( e ,"-->", c)
        e = box[i]
        c = 1
# print( e ,"-->", c)
    