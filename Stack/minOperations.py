class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []
        
        for val in logs:
            if val == '../':
                if stack:
                    stack.pop()
            
            elif val == './':
                print('do nothing')
            else: 
                stack.append(val)
                
        return len(stack)
