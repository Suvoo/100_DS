# https://youtu.be/htX69j1jf5U
# https://youtu.be/X2Ko1Jt9bL4

a = 10
b = 3

# INT_MAX = float('inf')
# INT_MIN = float('-inf')

INT_MAX = 2147483647
INT_MIN = - 2147483648


if a == INT_MIN and b == -1:
    print(INT_MAX)

dividend = a
divisor = b
a = abs(a)
b = abs(b)

ans = 0
while (a-b) >= 0:
    x = 0
    while a - ((b << 1) << x) >= 0:
        x+=1
    ans = ans + (1 << x) # how many times doubles
    a = a - (b << x)

sign = -1
if (dividend >= 0) == (divisor >= 0): #same sign
    sign = 1
print(ans * sign)




