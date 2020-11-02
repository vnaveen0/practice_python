class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        total_j = 0
        for val in S:
            if val in J:
                total_j +=1
        
        return total_j
    
