def countSubtreesWithSumX(root, x):
    def solve(root,x):
            
        if root is None: 
            return 0,0
        l,al = solve(root.left,x)
        r,ar = solve(root.right,x)

        su = l+r+root.data
        ans = al + ar

        if (su) == x:
            ans+=1
        return su,ans

    su,ans = solve(root,x)
    # print(su,ans)
    return ans