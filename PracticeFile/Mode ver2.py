d = [23,423,423,4234,343,34,23,23]

def count(lst ,el) :
    c = 0
    for i in lst :
        if el == i :
            c +=1
    return c


def mode(lst) :
    el_mode = lst[0]
    el_count = count(lst , lst[0])
    for e in lst :
        if el_count < count(lst, e) :
            el_mode = e
            el_count = count(lst, e )
    return el_mode

print("mode in this list = ", mode(d)) 