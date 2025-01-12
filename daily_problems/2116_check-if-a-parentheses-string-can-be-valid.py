class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        ul = []
        op = []
        for i in range(len(s)):
            if locked[i] == '0':
                ul.append(i)
            elif s[i] == "(":
                op.append(i)
            else:
                if op:
                    op.pop()
                elif ul:
                    ul.pop()
                else:
                    return False
        while op and ul and op[-1] < ul [-1]:
            op.pop()
            ul.pop()

        if op:
            return False
        return True

            


            


