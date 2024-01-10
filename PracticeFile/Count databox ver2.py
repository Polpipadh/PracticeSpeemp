data =  '123 123 423 423 42543212 121 12 231 23 4 43 1 4 33 234 2  2 2 3 4'

datalist = data.split()

box = [float(e) for e in datalist]
box.sort()

num = box[0] 
c =1

for i in range(1,len(box)) :
    if box[i] == num : 
        c += 1
    else :
        print(F"{box[i]} --> {c}")
        num = box[i]
        c = 1
        