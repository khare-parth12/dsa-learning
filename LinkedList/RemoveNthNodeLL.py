# Leetcode 19

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next == None: return None

        dummyHead = ListNode(-1, head)
        slow = dummyHead
        fast = dummyHead

        i = 0
        while i < n and fast.next != None:
            fast = fast.next
            i += 1

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next

        if slow.next == head:
            head = head.next
            return head
            
        temp = slow.next
        slow.next = temp.next
        temp.next = None

        return head