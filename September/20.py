# Problem
# https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1#

# References
# https://www.geeksforgeeks.org/factorial-large-number/

n = 4

arr = [1]

prod = 0
limit = 1
print(arr)
for x in range(2,n+1):
    carry = 0
    for i in range(limit):
        prod = (arr[i] * x) + carry
        arr[i] = prod % 10 # Store last digit of 'prod' in array 
        carry = prod // 10 # Put rest in carry

    while carry!=0:
        # arr[limit] = carry % 10
        arr.append(carry%10)
        carry = carry // 10
        limit+=1

print(arr[::-1])