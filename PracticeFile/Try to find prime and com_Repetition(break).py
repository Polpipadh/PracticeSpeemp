k = 0
Prime = []
Com = []
t = int(input()) = n 
for i in range(t) :
for k in range(2,n +1 ):
    if n%k ==0 : break
if k == n :
    Prime += str(n)
else :
    Com += str(n)
print("Prime = ",Prime)
print("Composit = ",Com)
