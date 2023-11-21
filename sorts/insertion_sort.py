from typing import List, Optional
from utils import printarResultadoEsperado


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{str(self.val)} - {str(self.next)}"


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_linked_list = None
        while node:
            node = head.next
            previous = sorted_linked_list

            if previous & previous.next < node.val:
                previous = previous.next



if __name__ == '__main__':
    s = Solution()
    linkedList = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    s.insertionSortList(linkedList)
    printarResultadoEsperado(linkedList, [1, 2, 3, 4])


