def canConstruct(self, ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    r = self.helper(ransomNote)
    m = self.helper(magazine)
    for s in r:
        if s not in m or r[s] > m[s]:
            return False
    return True


def helper(self, s):
    res = {}
    for i in s:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    return res