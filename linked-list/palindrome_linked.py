from typing import Optional

from utils import printarResultadoEsperado
from linkedList import ListNode, LinkedList


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palindrome = ''
        node = head
        while node is not None:
            palindrome += str(node.val)
            node = node.next
        print(palindrome)
        return palindrome == palindrome[::-1]


if __name__ == '__main__':
    s = Solution()
    linkedList = LinkedList()
    linkedList.add(1)
    linkedList.add(2)
    linkedList.add(2)
    linkedList.add(1)

    printarResultadoEsperado(s.isPalindrome(linkedList.head), True)