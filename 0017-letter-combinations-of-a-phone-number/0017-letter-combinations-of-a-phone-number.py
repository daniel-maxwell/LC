class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        mapping = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z"),
        }

        res = []

        def dfs(curr, i, j):
            print(curr)

            if len(curr) == len(digits):
                res.append(''.join(curr))
                return
            
            if i == len(digits) or j == len(mapping[digits[i]]):
                return

            curr.append(mapping[digits[i]][j])
            dfs(curr, i + 1, 0)
            curr.pop()
            dfs(curr, i, j + 1)

        dfs([], 0, 0)
        return res