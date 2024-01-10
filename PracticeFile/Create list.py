
# แบบต่อท้าย 

'''
print("How much number you want") 
n = int(input())
d = [] 
for i in range(n) :
    print("Import data #" , str(i+1) ,"here") 
    e = float(input())
    d.append(e)
print("Your d list = ", d)
'''
'''
# adding

print("How much number you want") 
n = int(input())
d = [0.0]*n
for i in range(n) :
    print("Import data #" , str(i+1) ,"here")
    e = float(input())
    d[i] = e
print("Your d list = ", d)

'''
'''
# out info try to get in loop 
d = [] 
e = input()
while e != 'stop' :
    d.append(float(e))
    e = input()
print(d) 
'''    
'''
# input info in loop but not recommend 
d = []
while True :
    x = float(input())
    if x == -1 :break
    d.append(x)
print(d) 
'''


'''
# use index but hard to use 
d = []
x = input().split()
for i in range(len(x)) :
    d.append(int(x[i])) 
print(d)
'''
d= []
x = input().split()
for e in x :
    d.append(int(e))
    
print(d) 


