n = int(input()) 
minx = int(input())
k = 0
while k < n+1 :
    x = int(input()) 
    if x< minx :
        minx = x
    k += 1
print(minx) 