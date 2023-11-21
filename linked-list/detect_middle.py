import math

from utils import printarResultadoEsperado


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{str(self.val)} - {str(self.next)}"


class Solution:
    def middleNode(self, head: ListNode) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    s = Solution()
    linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    resultado = s.middleNode(linkedList)
    printarResultadoEsperado(resultado, 5)
