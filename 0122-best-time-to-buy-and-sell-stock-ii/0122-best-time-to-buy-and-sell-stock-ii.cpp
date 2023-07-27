class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buyPrice = prices[0], profit = 0;

        for (int i = 0; i < prices.size(); ++i) {
            if (prices[i] > buyPrice) {
                profit += prices[i] - buyPrice;
                buyPrice = prices[i];
            }
            else if (prices[i] < buyPrice) {
                buyPrice = prices[i];
            };
        };
        return profit;
    };
};