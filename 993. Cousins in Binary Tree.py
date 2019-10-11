def isCousins(self, root, x, y):
    """
    :type root: TreeNode
    :type x: int
    :type y: int
    :rtype: bool
    """

    def helper(n, p):
        if n:
            d[n.val] = d[p.val] + 1 if p else 0
            parent[n.val] = p
            helper(n.left, n)
            helper(n.right, n)

    d = {}
    parent = {}
    helper(root, None)
    return d[x] == d[y] and parent[x] != parent[y]