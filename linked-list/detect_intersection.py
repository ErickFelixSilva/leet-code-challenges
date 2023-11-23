from typing import Optional

from linkedList import ListNode
from utils import printarResultadoEsperado


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        uniques = set()
        node = headA
        while node is not None:
            uniques.add(node)
            node = node.next
        node = headB
        while node is not None:
            if node in uniques:
                return node.val
            uniques.add(node)
            node = node.next
        return None


if __name__ == '__main__':
    s = Solution()

    common_node = ListNode(8, ListNode(4, ListNode(5)))
    head_1 = ListNode(4, ListNode(1, common_node))
    head_2 = ListNode(5, ListNode(6, ListNode(1, common_node)))

    resultado = s.getIntersectionNode(head_1, head_2)
    printarResultadoEsperado(resultado, 8)
