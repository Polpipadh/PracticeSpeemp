print("type list here")
x = input().split()
c = 0
i = 0
while i < len(x) :
    if int(x[i]) == 0 :
        c += 1
    i += 1
print(" 0 count = " ,c )