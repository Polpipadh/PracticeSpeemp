print("Import info you want") 
x = input().split()
d = []
for e in x :
    d.append(float(e))
d.sort()
# 0 1 2 3 
# 0 1 2 3 4 
if len(d) % 2 == 1 :
    print("Med of this info is =" , d[len(d)//2])
else : print("Med of this info is =" ,(d[len(d)//2]+d[len(d)//2-1])/2)

# "Med of this info is =" 