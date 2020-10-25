class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        lencost = len(cost)
        tcost = [None]*lencost
        tcost[0] = cost[0]
        tcost[1] = cost[1]
        
        for i in range(2, lencost):
            tcost[i] = cost[i] + min(tcost[i-1], tcost[i-2])
        
        
        mincost = min(tcost[lencost-1], tcost[lencost-2])
        return mincost
            
