print("how much number that you want to compair")
n = int(input())
k = 0
print("nubmer you want to compair")
minx = int(input())
while k < n-1:
    x = int(input())
    if x < minx :
        minx = x
    k +=1 
print("minx = " , minx) 