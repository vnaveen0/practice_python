class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        arr = [None]*(2*n)
        for i in range(0,n):
            j = n + i 
            idx = 2*i
            arr[idx] = nums[i]
            arr[idx+1] = nums[j]
            
        
        return arr
