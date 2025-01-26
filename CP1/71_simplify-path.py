import re
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = re.sub(r'[\/]+','/',path)
        path = path.split('/')
        path = [p for p in path if p!=""]
        new_path = []
        for p in path:
            if p == "..":
                if new_path:
                    new_path.pop()
            elif p == ".":
                pass
            else:
                new_path.append(p)
        if not new_path:
            return "/"
        new_pp = ["/"]
        for p in range(len(new_path)):
            new_pp.append(new_path[p])
            if p != len(new_path)-1:
                new_pp.append("/")
        return "".join(new_pp)