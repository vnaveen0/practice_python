class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LEN = len(nums)/2.0
        mem = {}
        for x in nums:
            if x in mem:
                mem[x] +=1
            else:
                mem[x] = 1
        
        for key, value in mem.items():
            if value > LEN:
                return key
