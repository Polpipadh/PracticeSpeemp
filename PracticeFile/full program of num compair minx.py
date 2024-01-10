print(" number of value you want to compair =")
n = int(input())
print("number compair here")
minx = float(input())
k = 0
while k < n - 1 :
    x = float(input())
    if x < minx :
        minx = x
    k += 1
print("min_x = " ,minx) 



