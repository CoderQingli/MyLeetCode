res = 0
def sumOfLeftLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.helper(root)
    return self.res

def helper(self, root):
    if not root:
        return
    if root.left and not root.left.left and not root.left.right:
        self.res += root.left.val
    self.sumOfLeftLeaves(root.left)
    self.sumOfLeftLeaves(root.right)