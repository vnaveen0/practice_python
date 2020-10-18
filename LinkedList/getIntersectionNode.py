# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        llA = headA
        llB = headB

        # Initial checks
        if llA is None or llB is None:
            return None

        # Find the length of the two LL
        lenA = 0
        while llA is not None:
            lenA += 1
            llA = llA.next

        lenB = 0
        while llB is not None:
            lenB += 1
            llB = llB.next

            # longer list runs ahead
        if lenA <= lenB:
            shorterLL = headA
            longerLL = headB
            diff = lenB - lenA
        else:
            shorterLL = headB
            longerLL = headA
            diff = lenA - lenB

        while diff > 0:
            longerLL = longerLL.next
            # update
            diff -= 1

        # now both are at same length
        while longerLL is not None:
            if longerLL is shorterLL:
                return longerLL
            else:
                # update
                longerLL = longerLL.next
                shorterLL = shorterLL.next

        return None


#---------------------------------------------
# Attempt 1: DID NOT READ THE WHOLE QUESTION
#---------------------------------------------
#         # Reverse a LL together O(n)
#         #---------------------------
#         lA = headA
#         lB = headB
#
#         # Initial checks
#         if lA is None and lB is None:
#             return None
#         if lA.next is None or lB.next is None:
#             if lA is lB and lA.next is None and lB.next is None:
#                 return lA
#             else:
#                 return None
#
#
#         prevA = ListNode()
#         prevA.val = lA.val
#         prevA.next = None
#         lA = lA.next
#
#         prevB = ListNode()
#         prevB.val = lB.val
#         prevB.next = None
#         lB = lB.next
#
#
#         while lA is not None or lB is not None:
#             if lA is not None:
#                 prev_prevA = ListNode()
#                 prev_prevA.val = lA.val
#                 prev_prevA.next = prevA
#                 # update
#                 prevA = prev_prevA
#                 lA = lA.next
#
#             if lB is not None:
#                 prev_prevB = ListNode()
#                 prev_prevB.val = lB.val
#                 prev_prevB.next = prevB
#                 # update
#                 prevB = prev_prevB
#                 lB = lB.next
#
#
#         lA = prevA
#         lB = prevB
#         #---------------------------
#         # iterate forward until you find a branch
#         #---------------------------
#
#         while lA is not None and lB is not None:
#             prev= lA
#             if lA is lB:
#                 # update
#                 lA = lA.next
#                 lB = lB.next
#             else:
#                 return prev
