class Solution:
    def simplifyPath(self, path: str) -> str:
        buffer, segments, pathArr = [], deque([]), ["/"]
        i = 0

        while i < len(path):       
            if path[i] == "/":
                if buffer:
                    if len(buffer) == 1 and buffer[0] == ".":
                        buffer.pop()
                    else:
                        segments.append(''.join(buffer))
                        buffer = []
            else:
                buffer.append(path[i])
            i += 1

        if buffer:
            if (len(buffer) == 1 and buffer[0] != ".") or len(buffer) > 1:
                segments.append(''.join(buffer))

        while segments:
            curr = segments.popleft()
            if curr == "..":
                if len(pathArr) > 1: pathArr.pop()
            else:
                pathArr.append(curr + "/")

        res = ''.join(pathArr)
        return res if len(res) == 1 else res[:-1]