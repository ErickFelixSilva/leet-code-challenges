from typing import Optional, List

from utils import printarResultadoEsperado
from linkedList import ListNode, LinkedList


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = dict(zip(nums, nums))
        node = head
        components_counter = 0
        currently_on_component = False
        while node is not None:
            value_in_nums = node.val in nums
            if value_in_nums and not currently_on_component:
                components_counter += 1
                currently_on_component = True
            elif not value_in_nums:
                currently_on_component = False

            node = node.next
        return components_counter


if __name__ == '__main__':
    s = Solution()
    # linkedList = LinkedList()
    # linkedList.add(0)
    # linkedList.add(1)
    # linkedList.add(2)
    # linkedList.add(3)
    #
    # printarResultadoEsperado(s.numComponents(head=linkedList.head, nums=[0, 1, 3]), 2)
    #
    # linkedList = LinkedList()
    # linkedList.add(0)
    # linkedList.add(1)
    # linkedList.add(2)
    # linkedList.add(3)
    # linkedList.add(4)
    # printarResultadoEsperado(s.numComponents(head=linkedList.head, nums=[0, 3, 1, 4]), 2)

    linkedList = LinkedList()
    linkedList.add(1)
    linkedList.add(2)
    linkedList.add(0)
    linkedList.add(4)
    linkedList.add(3)
    printarResultadoEsperado(s.numComponents(head=linkedList.head, nums=[3, 4, 0, 2, 1]), 1)
