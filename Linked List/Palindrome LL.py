# Leetcode 234

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        left = head
        numList = []

        while (left != None):
            numList.append(left.val)
            left = left.next
        
        l = 0
        r = len(numList) - 1
        while (l < r):
            if (numList[l] != numList[r]): return False
            l += 1
            r -= 1
        
        return True