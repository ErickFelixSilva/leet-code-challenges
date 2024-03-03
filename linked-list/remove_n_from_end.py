from typing import Optional, List

from utils import printarResultadoEsperado
from linkedList import ListNode, LinkedList


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        n_nodes_behind = None
        nodes_counter = 0
        while node is not None:
            nodes_counter += 1
            node = node.next

            if nodes_counter >= n + 1 and n_nodes_behind is None:
                n_nodes_behind = head
            elif nodes_counter >= n + 1 and n_nodes_behind is not None:
                n_nodes_behind = n_nodes_behind.next

        if nodes_counter == n:
            head = head.next
            return head
        if n_nodes_behind:
            n_nodes_behind.next = n_nodes_behind.next.next
        else:
            return ListNode(None)
        return head


if __name__ == '__main__':
    s = Solution()
    linkedList = LinkedList()
    linkedList.add(1)
    linkedList.add(2)
    linkedList.add(3)
    linkedList.add(4)
    linkedList.add(5)
    # printarResultadoEsperado(s.removeNthFromEnd(head=linkedList.head, n=2), [1,2,3,5])

    linkedList = LinkedList()
    linkedList.add(1)
    linkedList.add(2)
    linkedList.add(3)
    printarResultadoEsperado(s.removeNthFromEnd(head=linkedList.head, n=3), [])

    # linkedList = LinkedList()
    # linkedList.add(1)
    # linkedList.add(2)
    # linkedList.add(0)
    # linkedList.add(4)
    # linkedList.add(3)
    # printarResultadoEsperado(s.numComponents(head=linkedList.head, nums=[3, 4, 0, 2, 1]), 1)
