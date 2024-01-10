s = input()
t = ""
for ch in s:
    if "A" <= ch <= "Z" \
       or "a" <= ch <= "z" \
       or "0" <= ch <= "9" \
       or ch == ' ' :
        t += ch
print(t)

        