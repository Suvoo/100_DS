# Problem : https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1

# Aditya verma sliding window variation

from collections import Counter
txt = 'forxxorfxdofr'
pat = 'for'

dic = {}
i,j,a,ans = 0,0,0,0
k = len(pat)

for p in pat:
    if p in dic:
        dic[p] += 1
    else:
        dic[p] = 1
# dic = Counter(pat)

count = len(dic)

while(j < len(txt)):

    if txt[j] in dic:
        dic[txt[j]] -= 1
        if dic[txt[j]] == 0:
            count -= 1
    
    if j-i+1 < k:
        j+=1

    elif j-i+1 == k:
        if count == 0:
            ans += 1
        if txt[i] in dic:
            dic[txt[i]] += 1
            if dic[txt[i]] == 1:
                count += 1
        i+=1
        j+=1

print(ans)