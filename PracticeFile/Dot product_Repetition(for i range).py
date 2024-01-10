print('input vector U')
x = input().split() 
u =  [0]*len(x) 
for i in range(len(x)) :
    u[i]  = float(x[i]) 

print('input vector V')
x = input().split() 
v =  [0]*len(x) 
for i in range(len(x)) :
    v[i]  = float(x[i]) 
    
dot = 0
for i  in range(len(x)) :
    dot =   u[i]*v[i]
print(dot) 