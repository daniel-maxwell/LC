class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        for (int i = 0; i < prices.size() - 1; ++i) {
            int j = i + 1;
            while (j < prices.size() && prices[j] > prices[i]) ++j;
            if (j < prices.size()) {
                prices[i] -= prices[j];
            }
        }
        return prices;
    }
};