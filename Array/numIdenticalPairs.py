class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        N = len(nums)
        good = 0 
        for i in range(0, N-1):
            for j in range(i+1, N):
                if nums[i] == nums[j]:
                    good +=1
            
        return good

