class Solution {
public:
    const int maximumWealth(const vector<vector<int>>& accounts) {
        int largestBalance = 0;
        for (const vector<int> &row : accounts) {
            int currBalance = 0;
            for (const int &balance : row) {
                currBalance += balance;
            }
            largestBalance = max(largestBalance, currBalance);
        }
        return largestBalance;
    }
};