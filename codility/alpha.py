def solution(S):
    dic = {}
    cnt = 0
    for k in S:
        dic[k.lower()] = 0
    for c in S:
        if c.isupper():
            cl = c.lower()
            if dic[cl] == 0:
                dic[cl] = -1
            elif dic[cl] == 1:
                dic[cl] = 2
        else:
            if dic[c] == 0:
                dic[c] += 1
            elif dic[c] == 2:
                dic[c] = -1
    for k, v in dic.items():
        if v == 2:
            cnt += 1
    return cnt

print(solution("aaAbcCABBc"))
print(solution("xyzXYZabcABC"))
print(solution("ABCabcAefG"))