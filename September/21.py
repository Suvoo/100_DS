height = [2, 1, 5, 4, 6, 5]
n = len(height)

# 6
# 2 1 5 4 6 5
# op --> 10

i,j = 0,n-1
dist,current,mx = 0,0,0

while i<j:
    dist = j-i-1
    if height[i] > height[j]:
        current = height[j] * dist #right is smaller
        j-=1
    else:
        current = height[i] * dist #left is smaller
        i+=1
    mx = max(mx,current)

print(mx)