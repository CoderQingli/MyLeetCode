def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    s = ""
    for d in digits:
        s += str(d)
    num = int(s) + 1
    sp = str(num)
    res = []
    for i in sp:
        res.append(int(i))
    return res

    # def plusOne(self, digits):
    #     """
    #     :type digits: List[int]
    #     :rtype: List[int]
    #     """
    #     i = len(digits) - 1
    #     while i >= 0:
    #         if digits[i] < 9:
    #             digits[i] += 1
    #             break
    #         else:
    #             digits[i] = 0
    #             if i == 0:
    #                 digits.insert(0, 1)
    #                 break
    #             else:
    #                 i -= 1
    #     return digits