print("a =")
a = float(input())
l = 0
c = 0 
u = a 
x = (u+l)/2
while  abs(x**2-a) > 1e-10000000 *max(x**2,a)  :
    if x**2 < a :
        l = x
    else :
        u = x
    x = (u+l)/2
    c +=1
print("ans of a^0.5 = ", x)
print("total loops = ", c) 

    
