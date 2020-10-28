class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        N = len(mat)
        primary = 0 
        for i in range(0,N):
            primary += mat[i][i]
        
        secondary=0
        for j in range(0,N):
            secondary += mat[j][N-1-j]
        
        mid = N/2
        
        sum = primary + secondary
        
        if N%2 !=0: 
            sum = sum - mat[mid][mid]
        
        return sum 
        
