def __init__(self):
    self.total = 0


def convertBST(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root:
        self.convertBST(root.right)
        self.total += root.val
        root.val = self.total
        self.convertBST(root.left)
    return root