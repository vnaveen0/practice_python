class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        L = len(s)
        mid = L/2
        for idx in range(mid):
            # swap values             
            tmp = s[L-1-idx]
            s[L-1-idx] = s[idx]
            s[idx] = tmp
        
        return s
            
