print('vector u here')
x = input().split()
u = [float(e) for e in x]
print(f"your vector u = {u}") 
x = input().split()
v = [float(e) for e in x]
print(f"your vector v = {v}") 

dot = 0
for i in range(len(x)) :
    dot += u[i]*v[i]
print(f"dot pro = {dot}")

