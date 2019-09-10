def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    r = [root]
    res = [[root.val]]
    while r:
        tmp = []
        for i in range(len(r)):
            cur = r.pop(0)
            if cur.left:
                r.append(cur.left)
                tmp.append(cur.left.val)
            if cur.right:
                r.append(cur.right)
                tmp.append(cur.right.val)
        if len(tmp) != 0:
            res.append(tmp)
    return reversed(res)