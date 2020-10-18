# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def mergeTwoLists(self, l1, l2):
        def update_ptr(ptr, l):
            ptr.val = l.val
            ptr.next = None
            return ptr

        prev_ptr = None
        start_ptr = prev_ptr
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        while l1 is not None or l2 is not None:
            cur_ptr = ListNode()
            if l1 is None:
                prev_ptr.next = l2
                return start_ptr
            if l2 is None:
                prev_ptr.next = l1
                return start_ptr

            if l1.val <= l2.val:
                cur_ptr = update_ptr(cur_ptr, l1)
                l1 = l1.next
            else:
                cur_ptr = update_ptr(cur_ptr, l2)
                l2 = l2.next

            if prev_ptr is None:
                prev_ptr = cur_ptr
                start_ptr = prev_ptr
            else:
                prev_ptr.next = cur_ptr
                prev_ptr = prev_ptr.next

        return start_ptr






        return start_ptr

class ListNode(object):
    def __init__(self, val=None, ptr=None):
        self.val = val
        self.next = ptr

    def __str__(self):
        a = []
        start = self
        if start is None:
            return a.__str__()
        while(start is not None):
            a.append(start.val)
            start = start.next

        return a.__str__()


class LL(object):
    def __init__(self, ar):
        self. head = self.createLL(ar)

    def createLL(self, ar):
        len_ar = len(ar)
        prev = None
        for idx, val in reversed(list(enumerate(ar))):
            if idx == len_ar -1:
                prev = ListNode(val,None)
            else:
                l = ListNode(val, prev)
                prev = l
        return prev

    def print(self):
        a = []
        start = self.head
        while(start is not None):
            a.append(start.val)
            start = start.next

        print(a)


if __name__ == '__main__':
    s = Solution()
    ar1 = []
    ar2 = [4]

    l1 = LL(ar1)
    l2 = LL(ar2)
    l1.print()
    l2.print()

    ans = s.mergeTwoLists(l1.head, l2.head)
    print(ans)





