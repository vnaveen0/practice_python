class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        not_working = 0 
        
        N = len(nums)
        for idx in range(N-2):
            if nums[idx] > nums[idx+1]:
                if nums[idx] <= nums[idx+2]:
                    tochange= idx+1
                else: 
                    tochange = idx
                
                if tochange !=0 and nums[tochange-1] > nums[tochange+1]:
                    return False 
                
                not_working +=1
        
            
        if nums[N-2] > nums[N-1]:
            not_working +=1
        
        if not_working <=1:
            return True 
        else: 
            return False 
        
