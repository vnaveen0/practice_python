# Replace space with %20
# Ignore spaces in the end.

# String is immutable in python..
str = 'Mr  John Smith    '

str2 = ''
isfirst = True
for s in reversed(str):
    if s == ' ' and isfirst:
        continue

    elif s == ' ':
        str2 = '%20' + str2
    else:
        isfirst = False
        str2 = s + str2

print(str2)
