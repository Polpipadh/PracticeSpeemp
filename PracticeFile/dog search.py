data = "asd 987 asadf 987 asdf 897"


datadu = data.split()

dog = [] 
for i in range(0,len(datadu),2) :
    dog.append([datadu[i],datadu[i+1]])

print(dog)
check =True
search = input()

for [name,price] in dog :
    if search == name :
        print(price)

'''
for e in dog :
    if e[0] == search :
        print( search ,"=", e[1])
        check = False
'''
if check == True :
    print("Not found") 

# if search == datadu[i] :
#     check = False 
#     print(datadu[i+1])
# 	
# if search == True :
#     print('not found'
#           ) 
#

