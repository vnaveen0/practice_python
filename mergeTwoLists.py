# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start1 = l1
        start2 = l2
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        while (l1 is not None or l2 is not None):
            if l1 is None:
                return l2
            if l2 is None:
                return l1

            tmp1, tmp2 = self.merge(l1, l2)
            print(tmp1, tmp2)

        if start1.val <= start2.val:
            return start1
        else:
            return start2

    def merge(self, l1, l2):
        if l1.next is None and l2.next is None:
            if l1.val <= l2.val:
                l1.next = l2
            else:
                l2.next = l1

            return None, None

        elif l1.next is None and l2.next is not None:
            t2 = l2.next
            tmp2 = l2.next.next
            if l1.val <= l2.val:
                l1.next = l2
            else:
                l2.next = l1
                l2.next.next = t2
            return None, tmp2

        elif l2.next is None and l1.next is not None:
            t1 = l1.next
            tmp1 = l1.next.next
            if l1.val <= l2.val:
                l1.next = l2
                l1.next.next = t1
            else:
                l2.next = l1

            return tmp1, None
        else:
            # l1.next is not None and l2.next is not None
            tmp1 = l1.next.next
            tmp2 = l2.next.next
            t1 = l1.next
            t2 = l2.next
            v1_next = l1.next.val
            v2_next = l2.next.val
            v1 = l1.val
            v2 = l2.val
            if v1_next <= v2:
                # 2: v1, v1',v2,v2'
                l1.next.next = l2

            elif v2_next <= v1:
                # 3: v2,v2',v1,v1'
                l2.next.next = v1

            elif v1 <= v2:
                # 1: v1, v2, v1',v2'
                l1.next = l2
                l1.next.next = t1
                l1.next.next.next = t2

            elif v2 <= v1:
                # 4: v2, v1, v2',v1'
                l1 = l2
                l1.next = v1
                l1.next.next = t2
                l1.next.next.next = t1

            return tmp1, tmp2


class ListNode(object):
    def __init__(self, val, ptr):
        self.val = val
        self.next = ptr


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
    ar1 = [1,2]
    ar2 = [1]

    l1 = LL(ar1)
    l2 = LL(ar2)
    l1.print()
    l2.print()

    ans = s.mergeTwoLists(l1.head,l2.head)





