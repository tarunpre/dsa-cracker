
words = ["What","must","be","acknowledgment","shall","be"]
mxw = 16
cur, res, twl = [], [], 0
for w in words:
    #len of cur is for space
    if len(cur) + twl + len(w) > mxw:
        #new word for new line right now in loop
        #fix cur here
        for i in range(mxw-twl):
            cur[i%(len(cur)-1 or 1)] += " "
        res.append(''.join(cur))
        cur, twl = [],0

    cur += [w]
    twl += len(w)
print(res + [' '.join(cur).ljust(mxw)])

print("hello")

