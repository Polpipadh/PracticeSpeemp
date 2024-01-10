print("Import U list") 
x = input().split()
u = [0]*len(x)
for i in range(len(x)) :
    u[i] = float(x[i])
print("List u =", u )

for i in range(len(x)) :
    print("Add index #", str(i+len(x)) ,"here")  
    k = float(input()) 
    u.append(k)
    
print("List u after add k from back = ", u)


for i in range(len(x)) :
    print("What you want to delete") 
    g = float(input())
    if g in u :
        u.remove(g)
        print("Result u after delete", g, '=', u)
    else :
        print("Not found") 
