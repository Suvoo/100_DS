// Problem : https://practice.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1#

// References : https://www.youtube.com/watch?v=g6OxU-hRGtY


class Solution{
    public:
    // n: input to count the number of set bits
    //Function to return sum of count of set bits in the integers from 1 to n.
    int largestPowerof2(int n){
        int x = 0;
        while((1 << x) <= n) // gives largest power of 2 upto n also, 1 << x
            x+=1;
        return x-1;
    }
    
    int countSetBits(int n)
    {
        if(n==0)
            return 0;
            
        int x = largestPowerof2(n);
        //  1 -- > pow(2,x-1) * x
        int a1 = x *(1 << (x-1));
        // 2 --> n-pow(2,x) + 1
        int a2 = n - (1 << x) + 1;
        // 3 -- > remaining
        int a3 = n - (1 << x);
        int ans = a1 + a2 + countSetBits(a3);
        
        return ans;
        
    }
};