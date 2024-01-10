# function part
def dayinfeb(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return 29
    else:
        return 28

def dayinmonth(m, y):
    if m == 2:
        return dayinfeb(y)
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def dayinyear(y):
    if dayinfeb(y) == 29:
        return 366
    else:
        return 365

# input part
print("Input the year you want here:")
year = int(input())

months = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"]

print("Days in each month:")
for m in range(1, 13):
    print(f"{months[m-1]} --> {dayinmonth(m, year)}")

print(f"Total days in the year {year}: {dayinyear(year)}")
