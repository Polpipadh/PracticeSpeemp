data =  '123 123 423 423 42543212 121 12 231 23 4 43 1 4 33 234 2  2 2 3 4'

datalist = data.split()

#box = []
# for e in datalist :
#     box.append(float(e))
box = [float(e) for e in datalist]
box.sort()

print(box) 

e = box[0] 
c = 1
for i in range(1,len(box)) :
    if box[i] == e :
        c += 1 
        
    else :
        print( e ,"-->" , c)
        e = box[i]
        c = 1 