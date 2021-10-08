# https://practice.geeksforgeeks.org/problems/maximum-difference-of-zeros-and-ones-in-binary-string4111/1
# ref- pepcoding
S = "11111" 
# kadane gives max sum...so max 1s and -1s will give ans

	def maxSubstring(self, S):
		# code here
		S = list(S)
        for i in range(len(S)):
            if S[i] == '0':
                S[i] = 1
            else:
                S[i] = -1
        # print(S)
        
        local_mx = 0
        global_mx = -1
        
        for i in range(len(S)):
            # local_mx = max(local_mx,int(S[i])+local_mx)
            if local_mx > 0:
                local_mx = int(S[i])+local_mx
            else:
                local_mx = S[i]
                
            global_mx = max(global_mx,local_mx)
        
        return (global_mx)