# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1#
# STriver

class Solution:
    
    #Function to detect cycle in an undirected graph.
    def dfs(self,node,parent,vis,adj):
        vis[node] = 1
        for it in adj[node]:
            if vis[it] == 0:
                if self.dfs(it,node,vis,adj) == 1:
                    return True
            elif(it != parent):
                return True
                
        return False
            
        
	def isCycle(self, V, adj):
		#Code here
		vis = [0] * V
		for i in range(0,V):
		    if vis[i] == 0:
		        if self.dfs(i,-1,vis,adj) == 1:
		            return True
		return False