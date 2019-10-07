def leafSimilar(self, root1, root2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: bool
    """

    def helper(root):
        if root:
            if not root.left and not root.right:
                leave.append(root.val)
            helper(root.left)
            helper(root.right)

    leave = []
    helper(root1)
    tmp = leave
    leave = []
    helper(root2)
    return tmp == leave