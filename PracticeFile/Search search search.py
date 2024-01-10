data = "asd 987 asadf 987 asdf 897"
datalist = data.split()

name = datalist[0::2]
value = datalist[1::2]

print(name)
print(value) 
print("What you want to search") 
search = input()

# while search != 'stop' :
checkI = True
for i in range(len(name)): 
    if search == name[i] :
        checkI = False
        print(f"{search}  = {value[i]}")
if checkI == True :
    print("Not found")
    
print("want to find value lower than you want =  ") 
search2 = float(input())

lowerlist = []
check = True
for i in range(len(value)) :  
    if search2 > float(value[i]) :
        lowerlist.append(name[i]) 
        check = False

if check == True :
    print("Not found value lower than that")
else : print("comp that have value lower than ", search2, "=" ,lowerlist) 

