class Solution0(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

    
        def findsolns(n):
            if n==1:
                fn_x = 1
                fn_y = 0
                return fn_x, fn_y
            else:
                fnminus1_x, fnminus1_y = findsolns(n-1)
                fn_x = fnminus1_x + fnminus1_y
                fn_y = fnminus1_x
                return fn_x, fn_y 
            
        
        fnx, fny = findsolns(n)
        return fnx + fny 

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        
        if n==2:
            return 2
        
        dp = [None]*n
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n-1]
    
