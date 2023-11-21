from typing import Optional

from utils import printarResultadoEsperado


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{str(self.val)} - {str(self.next)}"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list: Optional[ListNode] = None
        if head is None:
            return None
        node = head
        while node.next is not None:
            reversed_list = ListNode(node.val, reversed_list)
            node = node.next
        reversed_list = ListNode(node.val, reversed_list)
        return reversed_list


if __name__ == '__main__':
    s = Solution()

    linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    resultado = s.reverseList(linkedList)
    printarResultadoEsperado(resultado, 5)

    resultado = s.reverseList(None)
    printarResultadoEsperado(resultado, 5)
