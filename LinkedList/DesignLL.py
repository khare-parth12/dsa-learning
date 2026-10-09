# Leetcode 707

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if head == None: return -1
        temp = head
        i = 0
        while i < index:
            if temp.next != None:
                temp = temp.next
                i += 1
            else:
                return -1

        return temp.val     

    def addAtHead(self, val):
        if head == None:
            head.val = val
            head.next = None

        else:
            temp = head.val
            head.val = val
            head.next = temp        

    def addAtTail(self, val):
        temp = head
        new_node = Node(val)
        while temp.next != None:
            temp = temp.next

        temp.next = new_node

    def addAtIndex(self, index, val):
        temp = head
        i = 0
        while i < index-1:
            if temp.next != None:
                temp = temp.next

    def deleteAtIndex(self, index):
        pass


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)