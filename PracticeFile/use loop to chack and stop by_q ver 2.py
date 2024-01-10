print("number you want to compair") 
minx = float(input())
e = input()
while e != 'q' :
    e = float(e)
    if e < minx :
        minx = e
    e = input()
print("minx = " ,minx)