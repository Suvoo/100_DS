# https://leetcode.com/problems/spiral-matrix

matrix = [  [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]
         ] 

n,m,k = 3,3,4

ans = []

rowStart,colStart = 0,0
rowEnd,colEnd = n - 1,m-1

while rowStart <= rowEnd and colStart <= colEnd:

    # Traverse Right
    for j in range(colStart,colEnd+1): 
        ans.append(matrix[rowStart][j])
    rowStart += 1
    # print(ans)

    # Traverse Down
    for i in range(rowStart,rowEnd+1):
        ans.append(matrix[i][colEnd])
    colEnd-=1
    # print(ans)

    if rowStart <= rowEnd:
        # Travel Left
        for j in range(colEnd,colStart-1,-1):
            ans.append(matrix[rowEnd][j])
    rowEnd-=1

    if colStart <= colEnd:
        # Travel Up
        for i in range(rowEnd,rowStart-1,-1):
            ans.append(matrix[i][colStart])
    colStart+=1

print(ans)
print(ans[k-1])