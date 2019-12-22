"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        divisor = 10
        dividend = l1.val + l2.val
        remainder = dividend % divisor
        quotient = dividend // divisor

        head = tail = ListNode(remainder)
        while (l1.next != None or l2.next != None):
            if (l1.next == None):
                l2 = l2.next
                dividend = quotient + l2.val
            elif (l2.next == None):
                l1 = l1.next
                dividend = quotient + l1.val
            else:
                l1 = l1.next
                l2 = l2.next
                dividend = quotient + l1.val + l2.val
            remainder = dividend % divisor
            quotient = dividend // divisor
            tail.next = ListNode(remainder)
            tail = tail.next

        if (quotient != 0):
            tail.next = ListNode(quotient)

        return head


if (__name__ == "__main__"):
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    obj = Solution()
    list = obj.addTwoNumbers(l1, l2)

    while (list != None):
        print(list.val)
        list = list.next
