class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(0, n+1):
            count = 0
            binaryNum = str(bin(i))

            for j in range(0, len(binaryNum)):
                if binaryNum[j] == "1":
                    count += 1

            ans.append(count)
   
        return ans   