s = str(input())
t = ''
for i in range(len(s)) :
    if "A" <= s[i] <= "Z" \
       or "a" <= s[i] <= "z" \
       or "0" <= s[i] <= "9" \
       or s[i] == ' ' :
        t += s[i]
print(t)
'''
for i in range(s) :
print(
'''
