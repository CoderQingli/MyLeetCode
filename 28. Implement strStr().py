def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle == "":
        return 0
    if haystack == "":
        return -1
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

# def strStr(self, haystack, needle):
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     if needle == "":
#         return 0
#     if len(haystack) < len(needle):
#         return -1
#     for i in range(len(haystack)-len(needle)+1):
#         if haystack[i:i+len(needle)] == needle:
#             return i
#     return -1