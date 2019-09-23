def findTheDifference(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    ds = self.helper(s)
    dt = self.helper(t)
    for i in dt:
        if i not in ds or dt[i] > ds[i]:
            return i


def helper(self, s):
    res = {}
    for i in s:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    return res