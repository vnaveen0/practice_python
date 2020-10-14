class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        for idx,val in enumerate(nums):
            if val != 0:
                nums[i] = val
                i+=1
        # i==3
        for k in range(i,len(nums)):
            nums[k] = 0
