def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    s = s.strip()
    res = s.split(" ")
    return len(res[-1])