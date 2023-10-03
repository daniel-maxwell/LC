class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = "." + dominoes + "."
        lStack, rStack, idxSet, = [], [], set()

        while True:
            for i in range(1, len(dominoes)-1):
                if i in idxSet: continue
                if dominoes[i] == ".":
                    left, right = dominoes[i-1], dominoes[i+1]
                    if left == "R" and right != "L":
                        rStack.append(i)
                        idxSet.add(i)
                    elif left != "R" and right == "L":
                        lStack.append(i)
                        idxSet.add(i)
                    else:
                        continue

            if not lStack and not rStack:
                break

            while lStack or rStack:
                if lStack:
                    idx = lStack.pop()
                    dominoes = dominoes[:idx] + "L" + dominoes[idx+1:]
                if rStack:
                    idx = rStack.pop()
                    dominoes = dominoes[:idx] + "R" + dominoes[idx+1:]

        return dominoes[1:-1]