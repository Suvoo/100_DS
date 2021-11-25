# (n+r-1)C(r-1)
import math

n = 2492 
k = 2141

if k > n:
	print(0)

MOD = 1000000007
ans = math.factorial(n-1)//(math.factorial(n-k) * math.factorial(k-1))
print(ans%MOD)
# print(math.factorial(0))