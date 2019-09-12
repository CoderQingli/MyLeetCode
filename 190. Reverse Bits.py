def reverseBits(self, n):
    tmp = str(bin(n)[2:])
    tmp = tmp[::-1]
    for i in range(32 - len(tmp)):
        tmp += "0"
    return int(tmp, 2)