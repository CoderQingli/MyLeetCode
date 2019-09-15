def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None
    right = self.invertTree(root.right)
    left = self.invertTree(root.left)
    root.right = left
    root.left = right
    return root