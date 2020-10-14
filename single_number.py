class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem = {}
        
        for x in nums:
            if x in mem:
                del mem[x]
            else: 
                mem[x]= 1
        
        for key, value in mem.items():
            return key
