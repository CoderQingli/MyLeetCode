def canPlaceFlowers(self, flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    if n < 1:
        return True
    if len(flowerbed) == 1:
        if flowerbed[0] == 0 and n <= 1:
            return True
        else:
            return False
    i = 1
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        n -= 1
        flowerbed[0] = 1
    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        n -= 1
        flowerbed[-1] = 1
    while i < len(flowerbed) - 1:
        if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            n -= 1
            flowerbed[i] = 1
        i += 1
    if n <= 0:
        return True
    else:
        return False