from typing import Optional

from utils import printarResultadoEsperado


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{str(self.val)} - {str(self.next)}"


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_middle: Optional[ListNode] = None
        slow = fast = head
        while fast and fast.next:
            previous_middle = slow
            slow = slow.next
            fast = fast.next.next
        if slow == fast:
            return None
        if previous_middle:
            previous_middle.next = previous_middle.next.next
        return head


if __name__ == '__main__':
    s = Solution()

    linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    resultado = s.deleteMiddle(linkedList)
    printarResultadoEsperado(resultado, 5)

    linkedList = ListNode(1)
    resultado = s.deleteMiddle(linkedList)
    printarResultadoEsperado(resultado, ListNode())
