def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs or "" in strs:
        return ""
    index = 0
    for i in range(len(min(strs))):
        s = set()
        for j in strs:
            s.add(j[i])
        if len(s) == 1:
            index += 1
        else:
            break
    return strs[0][:index]