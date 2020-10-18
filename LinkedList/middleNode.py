# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

            # traverse the LL
        len = 0
        ll = head
        while ll is not None:
            len += 1
            ll = ll.next

        # last index
        stopidx = len / 2

        ll = head
        for i in range(0, stopidx):
            ll = ll.next

        return ll