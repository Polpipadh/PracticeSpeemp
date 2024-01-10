point = [[2234,23234],[23423,234],[23423,2354]]

def dis(p1, p2) :
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (dx**2+dy**2)**0.5
        
def para(point) :
    long = 0
    for i in range(len(point)) :
        long += dis(point[i],point[(i+1)%len(point)])
    return long

print(para(point) ,"Unit" ) 

    