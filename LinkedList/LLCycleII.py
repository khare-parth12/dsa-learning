# Leetcode 142

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cycle_node = {}
        slow = head
        #fast = head

        while slow != None and slow.next != None:
            cycle_node[slow] = slow.next
            slow = slow.next
            #fast = fast.next.next

            if slow.next in cycle_node.keys(): return slow.next

        return None