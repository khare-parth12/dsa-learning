class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val):
        new_node = ListNode(val)
        curr = self.head
        new_node.next = curr
        self.head = new_node
             
    def addAtTail(self, val):
        self.addAtIndex(self.size, val)        

    def addAtIndex(self, index, val):
        if index > self.size:
            return

        if index == 0:
            self.addAtHead
        else:
            new_node = ListNode(val)
            curr = self.head
            for _ in range(index-1):
                curr = curr.next

            new_node.next = curr.next
            curr.next = new_node
        
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            curr = curr.next
        else:
            for _ in range(index-1):
                curr = curr.next

            curr.next = curr.next.next

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)