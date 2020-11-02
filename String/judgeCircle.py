class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        ValDict = {'U': 0, 'D': 0, 'L':0, 'R':0}
        
        for m in moves:
            ValDict[m] +=1
        
        if ValDict['U'] == ValDict['D'] and ValDict['L'] == ValDict['R']:
            return True
        else:
            return False
