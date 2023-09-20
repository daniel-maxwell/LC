class Solution:
    def reverse(self, x: int) -> int:

        x = str(x)
        rev = None

        if x[0] == '-':
            x = x[1:]
            rev = 0 - int(x[::-1])
        else:
            rev = x[::-1]


        if int(rev) > 2**31 or int(rev) < -2**31:
            return 0
        else:
            return int(rev)
        