# Leetcode 160

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        temp1 = headA
        temp2 = headB

        while temp1 is not temp2:
            # if temp1 is None: temp1 = headA
            # else: temp1 = temp1.next

            # if temp2 is None: temp2 = headB
            # else: temp2 = temp2.next

            temp1 =  headA if temp1 is None else temp1.next
            temp2 = headB if temp2 is None else temp2.next

        return temp1