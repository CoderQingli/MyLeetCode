class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        flag = 1
        if x < 0:
            x *= -1
            flag = -1
        while x:
            res = res * 10 + x % 10
            x /= 10
        return 0 if res > pow(2, 31) - 1 else res * flag