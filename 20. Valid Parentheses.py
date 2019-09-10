def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if s == "":
        return True
    stack = []
    top = ""
    mapping = {")": "(", "]": "[", "}": "{"}
    for item in s:
        if item in mapping:
            if stack:
                top = stack.pop()
                if top != mapping[item]:
                    return False
            else:
                return False
        else:
            stack.append(item)
    return not stack