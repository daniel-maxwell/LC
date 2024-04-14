class Solution:
    def splitString(self, s: str) -> bool:

        def validList(lst):
            prev = int(''.join(lst[0])) + 1
            for charList in lst:
                num = int(''.join(charList))
                if num >= prev or prev - num > 1:
                    return False
                prev = num
            return True


        def backtrack(curr, remS, preVal):
            if not remS:
                if len(curr) > 1:
                    if validList(curr):
                        return True
                return False

            nxt = []
            res = False
            
            for i in range(len(remS)):
                if res: break
                nxt.append(remS[i])
                if preVal and int(''.join(nxt)) != preVal - 1:
                    continue
                curr.append(nxt)
                res = res or backtrack(curr, remS[i+1:], int(''.join(nxt)))
                curr.pop()

            return res

        return backtrack([], s, None)