
data = "asd 987 asadf 987 asdf 897"
datasplit = data.split()
print('search here')
search = input()
check = False

if search in datasplit:
    i = datasplit.index(search)
    print(search , "=", datasplit[i+1])
    check = True
'''
for i in range(len(datasplit)) :
    if search == datasplit[i] :
        check = True
        print(search ,"=", datasplit[i+1])
'''

if check == False :
              print("Not found idiot what you looking at?")
              
name = datasplit[::2]
value = datasplit[1::2]
''''
#bruh
value = []
for e in datasplit[1::2] :
    value.append(float(e)) 
'''    
print("comp_name : ", name)
print("value of comp: ", value)


checker = False
lowwy = [] 
print("Value that lower that this")
lower = float(input())
for i in range(len(value)) :
    if lower > float(value[i]) :
        checker = True
        lowwy.append(name[i])
if checker == True :
    print("comp name that lower is = ", lowwy)
else : print("No comp that lower than that bro")



