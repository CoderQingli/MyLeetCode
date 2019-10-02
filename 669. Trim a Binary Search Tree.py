def trimBST(self, root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: TreeNode
    """

    def trim(root):
        if not root:
            return None
        if root.val > R:
            return trim(root.left)
        if root.val < L:
            return trim(root.right)
        else:
            root.left = trim(root.left)
            root.right = trim(root.right)
            return root

    return trim(root)