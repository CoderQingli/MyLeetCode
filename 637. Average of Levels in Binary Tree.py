def averageOfLevels(self, root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    if not root:
        return []
    q = [root]
    res = []
    tmpv = []
    tmpn = []
    while q:
        n = q.pop(0)
        tmpv.append(n.val)
        if n.left:
            tmpn.append(n.left)
        if n.right:
            tmpn.append(n.right)
        if not q:
            res.append(sum(tmpv) * 1.0 / len(tmpv))
            q = tmpn
            tmpn = []
            tmpv = []
    return res