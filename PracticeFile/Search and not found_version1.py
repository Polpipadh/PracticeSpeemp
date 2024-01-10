# "asd 987 asadf 987 asdf 897"

data = "asd 987 asadf 987 asdf 897"
datasplit = data.split()
print('search here')
search = input()
bruh = 'gg' 
for i in range(len(datasplit)) :
    if search == datasplit[i] :
        bruh = 'notgg'
        print(search ,"=", datasplit[i+1])
if bruh == 'gg' :
              print("not found")
