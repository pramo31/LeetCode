"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if (head == None):
            return None
        copy_list = []
        copy_linked_list = []
        while (head != None):
            copy_linked_list.append(head)
            copy_list.append([head.val, head.random])
            head = head.next

        deep_copy_list = [None] * len(copy_list)
        for i in range(0, len(copy_list)):
            deep_copy_list[i] = Node(copy_list[i][0])

        for i in range(0, len(copy_list)):
            if (copy_list[i][1] != None):
                random_node_index = copy_linked_list.index(copy_list[i][1])
                deep_copy_list[i].random = deep_copy_list[random_node_index]

        ret_head = tail = deep_copy_list[0]
        for i in range(1, len(deep_copy_list)):
            tail.next = deep_copy_list[i]
            tail = tail.next
        return ret_head


if (__name__ == "__main__"):
    node = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    basic_list = [None] * len(node)
    basic_list[0] = Node(node[0][0])
    for i in range(1, len(node)):
        basic_list[i] = Node(node[i][0])

    for i in range(0, len(node)):
        if (node[i][1] != None):
            basic_list[i].random = basic_list[node[i][1]]

    head = tail = basic_list[0]
    for i in range(1, len(basic_list)):
        tail.next = basic_list[i]
        tail = tail.next
    obj = Solution()

    result_head = obj.copyRandomList(None)
    while (result_head != None):
        print(result_head.val, result_head.next, result_head.random)
        result_head = result_head.next
