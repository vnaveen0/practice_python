class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        N = len(digits)
        carry = 1 
        corner= False
        for idx, val in reversed(list(enumerate(digits))):
                new_val = val + carry
                if new_val > 9: 
                    carry = new_val/10
                    digits[idx] = new_val % 10
                    
                else:
                    digits[idx] = new_val
                    carry = 0
                    break
        
        if carry != 0:
            digits.insert(0,carry)
            
                
        return digits 
            
