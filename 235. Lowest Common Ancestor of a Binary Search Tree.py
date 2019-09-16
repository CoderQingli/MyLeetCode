def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if p.val == q.val:
        return p
    if p.val < q.val:
        if p.val <= root.val and q.val >= root.val:
            return root
    else:
        if p.val >= root.val and q.val <= root.val:
            return root
    if p.val < root.val and q.val < root.val:
        root = root.left
    elif p.val > root.val and q.val > root.val:
        root = root.right
    return self.lowestCommonAncestor(root, p, q)