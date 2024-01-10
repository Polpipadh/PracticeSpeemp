#for Num input
N = int(input())

#for generate x list	

x = [0.0]*N
for i in range(N) :
    x[i] = float(input())

#for find mean
s = 0
for i in range(N) :
    s += x[i] 
mean = s/N

#for find SD 
s2 = 0
for i in range(N) :
    s2 += (x[i]-mean)**2
sd = (s2/N)**0.5

print(mean,sd) 
    