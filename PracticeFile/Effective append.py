# dot shit 
d1 = []
n = 40000
for i in range(n) :
    d1 = d1 + [i]
print(len(d1))

# Fast
d1 = []
n = 40000
for i in range(n) :
    d1 += [i]
print(len(d1))


# Fastest
d1 = []
n = 40000
for i in range(n) :
    d1.append(i) 
print(len(d1))



