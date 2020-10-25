class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
            
        if not nums:
            return 0 
        
        len_nums = len(nums)       
        if len_nums == 1:
            return nums[0]
        

        maxcost = [None]*len_nums

        
        maxcost[0] = nums[0]
        maxcost[1] = max(nums[0], nums[1])
        
        for i in range(2,len_nums):
            maxcost[i] = max( nums[i] + maxcost[i-2], maxcost[i-1])
        
        return max(maxcost[len_nums-1], maxcost[len_nums-2])
