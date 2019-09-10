import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = (re.sub(r"\W+", "", s)).lower()
        return string == string[::-1]

# import re
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         string = (re.sub(r"\W+", "", s)).lower()
#         l = 0
#         r = -1
#         while l < len(string)/2:
#             if string[l] != string[r]:
#                 return False
#             l += 1
#             r -= 1
#         return True