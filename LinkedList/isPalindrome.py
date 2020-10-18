# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # Find length of the LL
        len = 0
        ll = head

        if ll is None:
            return True
        elif ll.next is None:
            return True

        while ll is not None:
            len += 1
            ll = ll.next

        # Find stop point.
        stop = len / 2

        # Reverse the LL until the stopidx = floor(n/2)-1
        prev = head
        ll = head
        ll = ll.next

        for i in range(1, stop):
            # reverse LL
            pp = ll
            tmp = ll.next

            # update
            pp.next = prev
            ll = tmp
            prev = pp

        # now match the rest of the LL
        newll = prev
        if len % 2 != 0:
            # skip one elem
            ll = ll.next

            # match all elements
        while ll is not None:
            if ll.val != newll.val:
                return False
            else:
                ll = ll.next
                newll = newll.next

        return True
