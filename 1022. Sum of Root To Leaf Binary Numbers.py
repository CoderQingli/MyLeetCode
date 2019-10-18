def sumRootToLeaf(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def helper(n, s):
        if not n:
            return 0
        s = s * 2 + n.val
        if n.left or n.right:
            return helper(n.left, s) + helper(n.right, s)
        else:
            return s

    res = helper(root, 0)
    return res