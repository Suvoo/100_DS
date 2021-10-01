# Problem : https://practice.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1#

#References : https://www.youtube.com/watch?v=g6OxU-hRGtY

def LargestPowerOf2(n):
    x = 0 
    while((2**x) <= n): #gives power of 2 also, 1 << x
        x+=1    
    return x-1


def solve(n):
    if n == 0: 
        return 0

    x = LargestPowerOf2(n)
    # 1 -- > pow(2,x-1) * x
    a1 = x * (2 ** (x-1)) # also 1 << x
    # 2 --> n-pow(2,x) + 1
    a2 = n - 2**x + 1 
    # 3 -- > remaining
    a3 = n - (2**x)
    ans = a1 + a2 + solve(a3)
    return int(ans)

n = 51 # OP --> 140
ans = solve(n)
print(ans)