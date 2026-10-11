# Leetcode 203

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeElements(self, head, val):
        if head == None: return head

        prev = ListNode(0, head)
        curr = prev
        while curr != None:
            while curr.next != None and curr.next.val == val:
                curr.next = curr.next.next
            
            curr = curr.next

        return prev.next