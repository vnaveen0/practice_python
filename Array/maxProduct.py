class Solution0(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        g_max = -99999 
        N = len(nums)
        for i in range(0, N-1):
            for j in range(i+1, N):
                max = (nums[i]-1)*(nums[j]-1)
                
                if g_max < max:
                    g_max = max
        
        return g_max

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums)
        nums = sorted(nums)
        
        return (nums[N-2]-1)* (nums[N-1]-1)
