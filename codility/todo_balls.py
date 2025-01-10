def solution(S):
    if not 'R' in S or S.count('R') == 1:
        return 0
    if len(S) == 2:
        return 0
    red_positions = []
    for i in range(len(S)):
        if S[i] == 'R':
            red_positions.append(i)

    s = 0
    for r in range (1,len(red_positions)):
        s += red_positions[r] - red_positions[r-1] -1

    print(s)


print(solution("WRRWWWWWWWWRW"))
