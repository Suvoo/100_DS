# MAXSUM actually doesnt matter

from collections import defaultdict

def FindSum(n):
    s = list(str(n))
    s = [int(i) for i in s]
    su = sum(s)
    return su

N = 5
arr = [55,23,32,46,88]
# arr = [12,21,12]


dicc = defaultdict(list) # faster and more features than defaultdict

for i in arr:
    su = FindSum(i)    
    dicc[su].append(i)
print(dicc) 

if len(dicc) == len(arr):
    print(-1)

mx = 0
for i in dicc:
    print(dicc[i])
    if len(dicc[i]) < 2:
        continue
    dicc[i].sort()
    finSum = dicc[i][-1] + dicc[i][-2]
    # print(finSum)
    mx = max(mx,finSum)
print(mx)



