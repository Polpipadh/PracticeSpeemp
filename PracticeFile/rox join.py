rox = []

for k in range(1,31) :
    if k%5==0 or k%7==0 :
        rox.append(str(k))
print(':'.join(rox))

