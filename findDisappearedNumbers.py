# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         alist = list(range(1,len(nums)+1))
        
#         for x in nums:
#             if x in alist:
#                 alist.remove(x)
        
#         return alist
    
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        adict = {}
        for i in range(1,len(nums)+1):
            adict[i] = False
            
        
        for x in nums:
            if x in adict:
                adict[x] = True
        
        ans_list = []
        for key, val in adict.items():
            if not val:
                ans_list.append(key)
        
        return ans_list
