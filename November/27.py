'''
Step 1: Find m^(1/n) and round to integer as x
Step 2: Test if x^n = m

'''

n,m = 3,9
n,m = 6,4096

x = m**(1/n)
x = round(x)
print(x)

if x**n == m:
    print(x)
else:
    print(-1)