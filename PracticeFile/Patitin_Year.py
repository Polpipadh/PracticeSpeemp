def day_in_feb(y) :
    if y %400 or (y%4 and y%100 != 0 )  :
        return 29
    else :
        return 28
def day_in_month(m,y) :
    if m == 2 :
        return day_in_feb(y)
    if m	 in [4,6,9,11] :
        return 30
    else :
        return 31

def days_in_year (y) :
    if day_in_feb(y) == 29 :
        return 366
    else :
        return 365

print(days_in_year (29434))

for m in range(1,13) :
    print(day_in_month(m,2234))
    
        