# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None or head.next.next is None:
            return False

        n = head.next
        nn = head.next.next

        while 1:

            if n is nn:
                return True

            # update iterators
            if nn.next is None:
                return False
            elif nn.next.next is None:
                return False
            else:
                n = n.next
                nn = nn.next.next
