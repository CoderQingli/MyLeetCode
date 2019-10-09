def hasGroupsSizeX(self, deck):
    """
    :type deck: List[int]
    :rtype: bool
    """
    dic = {}
    for i in deck:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    size = dic[min(dic, key=dic.get)]
    if size < 2:
        return False
    ansbox = [size]
    for n in range(2, size / 2 + 1):
        if size % n == 0:
            ansbox.append(n)
    flag = True
    for k in ansbox:
        for i in dic:
            if dic[i] % k != 0:
                flag = False
                break
            if not flag:
                break
        if flag:
            return True
        flag = True
    return False