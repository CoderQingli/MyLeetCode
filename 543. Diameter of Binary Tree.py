def diameterOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    self.ans = 0

    def depth(n):
        if not n:
            return 0
        L = depth(n.left)
        R = depth(n.right)
        self.ans = max(self.ans, L + R + 1)
        return max(L, R) + 1

    depth(root)
    return self.ans - 1