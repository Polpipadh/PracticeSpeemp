minx = float(input())
e = float(input())
while e != 'q' :
    e = float(e)
    if e < minx :
        minx = e
    e = input()
print(minx) 