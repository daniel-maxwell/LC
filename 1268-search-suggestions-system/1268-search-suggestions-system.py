class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        charMap = { "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,
                    "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17,
                    "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
                    "z": 26,
        }

        def findIndex():
            l, r = 0, len(products) - 1
            res = -1

            while l <= r:
                mid = l + ((r - l) // 2)
                comparison = 0
                for i in range(len(currWord)):
                    a = charMap[currWord[i]]
                    b = charMap[products[mid][i]] if i < len(products[mid]) else -1
                    if a > b:
                        comparison = 1
                        break
                    elif a < b:
                        comparison = -1
                        break

                if comparison == -1: r = mid - 1
                elif comparison == 1: l = mid + 1
                else: res, r = mid, mid - 1

            return res
        

        currWord, res = "", []

        for char in searchWord:
            currWord += char
            currRes, startIdx = [], findIndex()
            
            if startIdx == -1:
                res.append(currRes)
                continue
            
            currRes.append(products[startIdx])
            i = 1
            while startIdx + i < len(products) and len(currRes) < 3:
                if products[startIdx + i][:len(currWord)] == currWord:
                    currRes.append(products[startIdx + i])
                else:
                    break
                i += 1

            res.append(currRes)

        return res