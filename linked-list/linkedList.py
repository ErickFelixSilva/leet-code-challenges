class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        new_node = ListNode(item)
        if self.head is None:
            self.head = new_node
            return
        if self.head.next is None:
            self.head.next = new_node
            return
        last_node = self.head.next
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{str(self.val)} - {str(self.next)}"