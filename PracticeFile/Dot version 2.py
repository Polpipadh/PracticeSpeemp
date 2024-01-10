print("input vector u here")

x = [float(i) for i in input().split()]  

u  = [0]*len(x)
for i in range(len(x)) :
    u[i] = x[i]
    

print("vector u =", u)

x = [float(i) for i in input().split()]  

print("inpout vector v here") 
v  = [0]*len(x)
for i in range(len(x)) :
    v[i] = x[i]

print("vector v =", v)

def dot(u, v) :    
    d = 0
    for i in range(len(x)) :
        d += u[i]*v[i]
    return d

print("dot = ",dot(u, v) )
