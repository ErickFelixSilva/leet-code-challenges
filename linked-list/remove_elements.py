from typing import Optional

from utils import printarResultadoEsperado


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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{str(self.val)} - {str(self.next)}"


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        node = head
        previous_node: Optional[ListNode] = None
        while node is not None:
            if node.val == val and previous_node:
                node = previous_node.next = node.next
                continue
            elif node.val == val and not previous_node:
                node = head = node.next
                continue
            previous_node = node
            node = node.next
        return head


if __name__ == '__main__':
    s = Solution()

    # linkedList.py = LinkedList()
    # linkedList.py.add(1)
    # linkedList.py.add(2)
    # linkedList.py.add(6)
    # linkedList.py.add(3)
    # linkedList.py.add(4)
    # linkedList.py.add(5)
    # linkedList.py.add(6)
    # resultado = s.removeElements(linkedList.py.head, 6)
    # printarResultadoEsperado(resultado, 6)

    linkedList = LinkedList()
    linkedList.add(1)
    linkedList.add(2)
    linkedList.add(2)
    linkedList.add(1)
    resultado = s.removeElements(linkedList.head, 2)
    printarResultadoEsperado(resultado, None)

