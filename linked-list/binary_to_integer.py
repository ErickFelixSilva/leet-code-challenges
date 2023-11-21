from utils import printarResultadoEsperado


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{str(self.val)} - {str(self.next)}"


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        number = ''
        node = head
        while node.next is not None:
            number = number + str(node.val)
            node = node.next
        number = number + str(node.val)
        return int(number, 2)


if __name__ == '__main__':
    s = Solution()
    linkedList = ListNode(1, ListNode(0, ListNode(1)))
    s.getDecimalValue(linkedList)
    printarResultadoEsperado(s.getDecimalValue(linkedList), 5)