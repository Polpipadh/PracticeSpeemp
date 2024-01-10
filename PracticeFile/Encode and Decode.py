def rot_14(x):
    x = x.upper()
    gg = '' 
    ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in x :
        if "A" <= i <= "Z" :
            gg += ch[(ch.find(i)+14)%26]
        else : gg += str(i)
    return gg





def crack(x):
    x = x.upper()
    gg = '' 
    ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in x :
        if "A" <= i <= "Z" :
            gg += ch[(ch.find(i)-14)%26]
        else : gg += str(i)
    return gg

inin = rot_14(input()) 
print("Encode:",inin)
cinin = crack(inin) 
print("Decode :",cinin)

