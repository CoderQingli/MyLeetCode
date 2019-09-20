def getSum(self, a, b):
    carry = 0
    mask = 0xffffffff
    while b & mask != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry

    # for overflow condition like
    # -1
    #  1
    return a & mask if b > mask else a