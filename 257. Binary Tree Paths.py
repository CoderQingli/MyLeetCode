def binaryTreePaths(self, root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    paths = []
    self.helper(root, [], paths)
    return ["->".join(str(val) for val in path) for path in paths]


def helper(self, root, path, paths):
    if not root:
        return
    path.append(root.val)
    if not root.left and not root.right:
        paths.append(path)
        return
    self.helper(root.left, path[:], paths)
    self.helper(root.right, path, paths)