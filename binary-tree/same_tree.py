from typing import Optional

from utils import printarResultadoEsperado


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.printTree(p, q)

    def traverseTree(self, p: TreeNode, q: TreeNode):
        if p is None and q is None:
            return True
        if (p is None) != (q is None):
            return False
        if p.val != q.val:
            return False
        return self.printTree(p.right, q.right) and self.printTree(p.left, q.left)


if __name__ == '__main__':
    s = Solution()
    # left = TreeNode(1, TreeNode(2), TreeNode(3))
    # right = TreeNode(1, TreeNode(2), TreeNode(3))
    # printarResultadoEsperado(s.isSameTree(left, right), True)
    # left = TreeNode(1, TreeNode(2))
    # right = TreeNode(1, None, TreeNode(2))
    # printarResultadoEsperado(s.isSameTree(left, right), False)
    # left = TreeNode(1, TreeNode(2), TreeNode(1))
    # right = TreeNode(1, TreeNode(1), TreeNode(2))
    # printarResultadoEsperado(s.isSameTree(left, right), False)
    left = TreeNode(2, None, TreeNode(4))
    right = TreeNode(2, TreeNode(3), TreeNode(4))
    printarResultadoEsperado(s.isSameTree(left, right), False)
    # printarResultadoEsperado(s.isSameTree(None, TreeNode(0)), False)
    # printarResultadoEsperado(s.isSameTree(None, None), True)
