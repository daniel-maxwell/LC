class Solution:
    def totalMoney(self, n: int) -> int:
        balance = 1
        deposits = {0: 1}

        for d in range(1, n):
            depositAmt = 0
            weekDay = d % 7
            if weekDay == 0:
                balance += deposits[0] + 1
                depositAmt = deposits[0] + 1

            else:
                balance += deposits[weekDay - 1] + 1
                depositAmt = deposits[weekDay - 1] + 1

            deposits[weekDay] = depositAmt

        return balance