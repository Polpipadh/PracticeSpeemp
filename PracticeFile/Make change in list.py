import math


x  = [] 
for i  in range(1,10) :
    x.append(math.pi/i)
    

def listsin(x) :
    s =  [ math.sin(k) for k in x]
    return s 
    
    
print(listsin(x))