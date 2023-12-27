class Solution:
    def validateIP(self, ip):
        sub, numDots = [], 0

        def checkSub(sub):
            if not sub: return False
            if len(sub) > 3: return False
            if sub[0] == "0" and len(sub) > 1: return False
            subSum = int(''.join(sub))
            if subSum < 0 or subSum > 255: return False
            return True

        for i in range(0, len(ip)):
            if ip[i] == ".":
                if not checkSub(sub): return False
                sub = []
                numDots += 1
            else:
                sub.append(ip[i])
        return numDots == 3 and checkSub(sub)

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []
        res = []

        def backtrack(currIP, i, dots):
            if i == len(currIP): return
            currIP = currIP[:i] + "." + currIP[i:]
            dots -= 1
            
            if dots == 0:
                if self.validateIP(currIP):
                    res.append(currIP)
                currIP = currIP[:i] + currIP[i+1:]
                backtrack(currIP, i+1, 1)
                return

            backtrack(currIP, i + 2, dots)
            currIP = currIP[:i] + currIP[i+1:]
            backtrack(currIP, i + 1, dots + 1)
            return
            
        backtrack(s, 1, 3)
        return res