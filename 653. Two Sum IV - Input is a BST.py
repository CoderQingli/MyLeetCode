def findTarget(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """
    if not root:
        return False
    self.root_val = []
    self.helper(root)
    i = 0
    j = len(self.root_val) - 1
    while i < j:
        if self.root_val[i] + self.root_val[j] == k:
            return True
        elif self.root_val[i] + self.root_val[j] > k:
            j -= 1
        else:
            i += 1
    return False


def helper(self, root):
    if not root:
        return
    self.helper(root.left)
    self.root_val.append(root.val)
    self.helper(root.right)
    return