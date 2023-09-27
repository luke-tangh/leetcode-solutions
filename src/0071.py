class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split('/')
        cpath = []
        for t in tokens:
            if t == "" or t == '.':
                continue
            elif t == "..":
                if len(cpath) > 0:
                    cpath.pop()
            else:
                cpath.append(t)
        return '/' + '/'.join(cpath)
