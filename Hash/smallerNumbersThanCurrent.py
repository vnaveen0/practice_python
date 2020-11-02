class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = sorted(nums)
        
        new_d = {}
        new_arr = []
        prev_val= [None, None]
        
        for idx, val in enumerate(arr):
            if val != prev_val[0] and val not in new_d:
                new_d[val] = idx

                    
        for val in nums:
            new_arr.append(new_d[val])
            
        return new_arr
