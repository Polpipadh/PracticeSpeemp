def rot_21(x) :
    Newpass = ""
    cha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for e in x :
        if "A" <= e <= "Z" :
            Newpass += cha[(cha.find(e) +21 )%26 ]
        else : Newpass += e  
    return Newpass


print(rot_21("SDAFKLDFSDFD") )