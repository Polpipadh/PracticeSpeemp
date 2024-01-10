
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
