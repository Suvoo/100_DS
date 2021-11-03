a = [5,3,2,4,1]

a.sort()
su = 0
MOD = 1000000007
for i in range(len(a)):
    su += i * a[i]
    su = su % MOD
print(su%MOD)
