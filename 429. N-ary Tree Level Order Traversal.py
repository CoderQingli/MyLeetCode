def levelOrder(self, root):
    """
    :type root: Node
    :rtype: List[List[int]]
    """
    if root:
        nodes = [root]
        res = []
        while len(nodes) > 0:
            t1 = []
            t2 = []
            for i in nodes:
                t1.append(i.val)
                for j in i.children:
                    if j is not None:
                        t2.append(j)
            if len(t1) > 0:
                res.append(t1)
            if len(t2) > 0:
                nodes = t2
            else:
                break
        return res
    else:
        return None
