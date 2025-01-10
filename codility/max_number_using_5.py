def solution(S, K):
    if K > len(S):
        return "IMPOSSIBLE"
    SL = list(S)
    for s in range(len(SL)):
        if K > 0:
            if int(SL[s]) < 5:
                SL[s] = '5'
                K -= 1
    for s in range(len(SL)-1, -1 , -1):
        if K > 0:
            if int(SL[s]) !=  5:
                SL[s] = '5'
                K -= 1

    if K:
        return "IMPOSSIBLE"
    return "".join(SL)


print(solution("165232", 3))
print(solution("1839550", 4))
print(solution("5567855", 4))