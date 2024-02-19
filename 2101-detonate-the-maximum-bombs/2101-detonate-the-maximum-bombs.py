class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def withinRange(a, b):
            t1 = abs(a[0]-b[0])
            t2 = abs(a[1]-b[1])
            return (t1**2) + (t2**2) <= a[2] ** 2

        i, res = 0, -1
        res = [-1, None]

        while i < len(bombs):
            q = deque([bombs[i]])
            visited = set([tuple(bombs[i])])
            detonations = 1
            while q:
                for _ in range(len(q)):
                    curr = q.pop()
                    for bomb in bombs:
                        if bomb == curr or tuple(bomb) in visited:
                            continue
                        else:
                            if withinRange(curr, bomb):
                                q.appendleft(bomb)
                                visited.add(tuple(bomb))
                                detonations += 1

            if detonations > res[0]:
                res[0] = detonations
                res[1] = bombs[i]
            i += 1

        cnt = 0
        for bomb in bombs:
            if bomb == res[1]:
                cnt += 1
            
        return res[0] + (cnt - 1)