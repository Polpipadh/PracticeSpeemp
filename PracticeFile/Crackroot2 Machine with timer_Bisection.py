import cProfile

def calculate_square_root():
    print("What you want to take root 2")
    a = float(input())
    L = 0
    U = a
    x = (U + L) / 2
    while x ** 2 != a:
        if x ** 2 < a:
            L = x
        else:
            U = x
        x = (U + L) / 2
    print(x)

# Run the code with cProfile
cProfile.run('calculate_square_root()')
