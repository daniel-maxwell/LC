class Solution:
    sys.set_int_max_str_digits(10500)
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        strNum = ""
        for i in range(0, len(num)):
            strNum += str(num[i])
        res = str(int(strNum) + k)
        output = [int(c) for c in res]
        return output