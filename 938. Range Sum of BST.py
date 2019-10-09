def rangeSumBST(self, root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: int
    """

    def helper(n):
        if not n:
            return
        if L <= n.val <= R:
            self.res += n.val
        if L < n.val:
            helper(n.left)
        if R > n.val:
            helper(n.right)

    self.res = 0
    helper(root)
    return self.res