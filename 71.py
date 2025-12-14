class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        s = []
        for d in dirs:
            if d == '' or d == '.':
                continue
            if d == '..':
                if s:
                    s.pop()
            else:
                s.append(d)
        return '/' + '/'.join(s)
