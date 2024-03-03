from typing import Optional

from utils import printarResultadoEsperado


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    diameters = []

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameters = []
        self.maxDepth(root)
        return max(self.diameters)

    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        else:

            lDepth = self.maxDepth(node.left)
            rDepth = self.maxDepth(node.right)

            self.diameters.append(lDepth + rDepth)
            print(self.diameters)

            if (lDepth > rDepth):
                return lDepth + 1
            else:
                return rDepth + 1


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    printarResultadoEsperado(s.diameterOfBinaryTree(root), 3)
    root = TreeNode(1)
    root.left = TreeNode(2)
    printarResultadoEsperado(s.diameterOfBinaryTree(root), 1)
