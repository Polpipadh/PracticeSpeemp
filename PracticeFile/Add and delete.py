
print("Import U list") 
x = input().split()  # Corrected the use of split()
u = [float(item) for item in x]  # Use list comprehension to convert input to float
print("List u =", u )

for i in range(len(x)) :
    print("Add here (Add #)", str(i)) 
    k = float(input())  # Convert user input to float
    u.append(k)
    
print("List u after add k = ", u)
