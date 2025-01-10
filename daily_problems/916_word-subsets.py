class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        dk = {}
        for w in words2:
            for i in w:
                if i in dk:
                    dk[i] = max(dk[i], w.count(i))
                else:
                    dk[i] = 1
        fin = []
        for w in words1:
            fin.append(w)
            for k,v in dk.items():
                if not w.count(k) >= v:
                    fin.pop()
                    break
        return fin


        
        