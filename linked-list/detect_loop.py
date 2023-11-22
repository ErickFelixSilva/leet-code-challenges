from typing import Optional

from linkedList import ListNode
from utils import printarResultadoEsperado


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        uniques = set()
        node = head
        while node is not None:
            if node in uniques:
                return node
            uniques.add(node)
            node = node.next
        return None


if __name__ == '__main__':
    s = Solution()

    tail = ListNode(-4)
    looped_node = ListNode(2, ListNode(0, tail))
    tail.next = looped_node

    resultado = s.hasCycle(ListNode(3, looped_node))
    printarResultadoEsperado(resultado, True)
