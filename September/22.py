# https://practice.geeksforgeeks.org/problems/0cba668df04d657fde4d1bd28b626a01e61097f1/1#

A = "abcd"
B = "cdabcdab"

# A = 'aa'
# B = 'a'

# A = 'ab'
# B = 'cde'

temp = ''
c = 0

while len(temp) < len(B):
    temp+=A
    c+=1
    if B in temp:
        break

# print(temp)

if B in temp:
    print(c)
else:
    temp+=A
    if B in temp:
        print(c+1)
    else:
        print(-1)
