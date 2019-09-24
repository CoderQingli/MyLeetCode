cnt = 0
def pathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """
    if not root:
        return 0
    self.helper(root, [root.val], sum)
    return self.cnt

def helper(self, root, s, sum):
    self.cnt += s.count(sum)
    if root.left:
        self.helper(root.left, [x + root.left.val for x in s] + [root.left.val], sum)
    if root.right:
        self.helper(root.right, [x + root.right.val for x in s] + [root.right.val], sum)