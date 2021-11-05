a1 = [11, 1, 13, 21, 3, 7]
a2 = [11, 3, 7, 1]

c = 0
for i in a2:
    if i in a1:
        c+=1
if c == len(a2):
    print('yes')
else:
    print('no')
