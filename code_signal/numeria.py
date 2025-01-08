#find pairs where numbers are identical in length and differ by exactly one digit

nums = [1, 151, 241, 1, 9, 22, 351]
def chk(n1, n2):
    diff = 1
    same = len(n1) - diff
    df = 0
    sm = 0
    for j in range(len(n1)):
        if n1[j] == n2[j]:
            sm += 1
        else:
            df += 1
    if sm == same and df == diff:
        return True

    
res = 0
for x in range(len(nums)):
    for m in range(x+1, len(nums)):
        #chk x with all m
        s1 = str(nums[x])
        s2 = str(nums[m])
        if len(s1) == len(s2) and nums[x] != nums[m]:
            if chk(s1, s2):
                res += 1

print(res)