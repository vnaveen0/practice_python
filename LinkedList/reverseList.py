# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        prev = ListNode()
        prev.val = head.val
        prev.next = None
        orig_ll = head.next

        while orig_ll is not None:
            prev_prev = ListNode()
            prev_prev.val = orig_ll.val
            prev_prev.next = prev

            # update iterators
            prev = prev_prev
            orig_ll = orig_ll.next

        return prev
