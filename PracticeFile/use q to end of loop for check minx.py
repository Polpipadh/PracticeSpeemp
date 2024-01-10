minx = int(input())
e = input()
while e != "q" :
    x = float(e)
    if x < minx :
        minx = x
    e = input()
print(minx) 