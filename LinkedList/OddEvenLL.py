# Leetcode 328

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        if head == None or head.next == None: return head

        evenHead = head.next
        even = head.next
        odd = head
        while even != None and even.next != None:
            odd.next = even.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = evenHead

        return head