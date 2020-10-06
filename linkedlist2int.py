# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        num = []
        while(head.next != None):
            num.append(head.val)
            head = head.next
        
        num.append(head.val)
        
        f_idx=0
        total=0
        print(num)
        for rev_idx in range(len(num)-1,-1,-1):
            total += num[rev_idx]*pow(2,f_idx)
            f_idx +=1
        return total
            
        
