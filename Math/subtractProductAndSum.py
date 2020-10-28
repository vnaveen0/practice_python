class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product =1
        sum=0
        
        while(n!=0):
            digit = n%10
            print(digit)
            product = product*digit
            sum = sum + digit            
            n = n/10 
            
 
        # print('prod:{} sum:{}'.format(product, sum))
        return product - sum 
            
