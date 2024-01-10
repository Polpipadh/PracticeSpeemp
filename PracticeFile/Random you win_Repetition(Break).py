import random
numprice = random.randint(1,99)
print("you have 9 tries")
for i in range(1,10) :
    print("Enter you num #", str(i))
    guess = int(input())
    print("#" ,str(i))
    if guess > numprice : print("It Lower")
    if guess < numprice : print("It upper")
    if guess == numprice : break
if guess == numprice :
    print('You Win')
else : print("You diff") 