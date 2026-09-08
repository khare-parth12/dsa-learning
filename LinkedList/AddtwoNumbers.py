# Leetcode 2

def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummyHead = ListNode()
        tail = dummyHead
        carry = 0
        while (l1 is not None or l2 is not None or carry!=0):
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            sum = digit1 + digit2 + carry
            new_node = ListNode(sum%10)
            carry = sum//10
            tail.next = new_node
            tail = tail.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        l3 = dummyHead.next
        dummyHead.next = None
        return l3