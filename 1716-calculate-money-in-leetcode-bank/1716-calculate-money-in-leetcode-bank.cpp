class Solution {
public:
    int totalMoney(int n) {
        int balance = 0;
        int week = 1;
        while (n > 7) {
            balance += (week * 7) + 21;
            n -= 7;
            ++week;
        }
        int day = week;
        while (n > 0) {
            balance += day;
            ++day;
            --n;
        }
        return balance;
    }
};