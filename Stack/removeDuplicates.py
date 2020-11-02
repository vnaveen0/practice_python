
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for val in S:
            if not stack:
                stack.append(val)
            else: 
                y = stack[-1]
                if y == val:
                    stack.pop()
                else: 
                    stack.append(val)
        new_s = ''.join(stack)
        return new_s
