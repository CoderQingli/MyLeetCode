def isUnivalTree(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return False
    tmp = root.val
    flag = True

    def helper(n, flag):
        if n:
            if n.val != tmp:
                return False
            else:
                flag = helper(n.left, flag)
                flag = helper(n.right, flag)
        return flag

    return helper(root, flag)