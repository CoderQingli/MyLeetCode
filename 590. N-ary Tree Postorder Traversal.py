def postorder(self, root):
    """
    :type root: Node
    :rtype: List[int]
    """
    if not root:
        return []
    q = [root]
    res = []
    while q:
        tmp = q.pop()
        res.append(tmp.val)
        for c in tmp.children:
            if c:
                q.append(c)
    return res[::-1]