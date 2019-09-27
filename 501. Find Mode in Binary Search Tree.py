def __init__(self):
    self.dic = {}


def findMode(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return None
    self.helper(root)
    res = []
    max_val = max(self.dic.values())
    for k in self.dic:
        if self.dic[k] == max_val:
            res.append(k)
    return res


def helper(self, root):
    if not root:
        return root
    self.helper(root.left)
    if root.val in self.dic:
        self.dic[root.val] += 1
    else:
        self.dic[root.val] = 1
    self.helper(root.right)
    return