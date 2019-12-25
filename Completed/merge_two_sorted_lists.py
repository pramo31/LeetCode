"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 == None):
            return l2
        elif (l2 == None):
            return l1
        else:
            head = None
            if (l1.val < l2.val):
                head = ListNode(l1.val)
                l1 = l1.next
            else:
                head = ListNode(l2.val)
                l2 = l2.next
            tail = head
            while (l1 != None and l2 != None):
                if (l1.val < l2.val):
                    tail.next = ListNode(l1.val)
                    l1 = l1.next
                elif (l1.val > l2.val):
                    tail.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    tail.next = ListNode(l1.val)
                    tail = tail.next
                    tail.next = ListNode(l2.val)
                    l1 = l1.next
                    l2 = l2.next
                tail = tail.next
            if (l1 != None):
                while (l1 != None):
                    tail.next = ListNode(l1.val)
                    l1 = l1.next
                    tail = tail.next
            if (l2 != None):
                while (l2 != None):
                    tail.next = ListNode(l2.val)
                    l2 = l2.next
                    tail = tail.next
            return head


if (__name__ == "__main__"):
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)

    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)

    obj = Solution()
    lst = obj.mergeTwoLists(l1, l2)

    while (lst != None):
        print(lst.val, end='')
        lst = lst.next
