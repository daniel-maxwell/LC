class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {

        vector<int> coinsRequired {0};
        unordered_set<int> coinSet (coins.begin(), coins.end());

        for (int i = 1; i <= amount; ++i) {
            if (coinSet.contains(i)) {
                coinsRequired.push_back(1);
                continue;
            }
            int minCoins = amount + 1;
            for (const int &c : coins) {
                if (i - c >= 0 && coinsRequired[i - c] != -1) {
                    minCoins = min(minCoins, coinsRequired[i - c] + 1);
                }
            }
            minCoins = minCoins <= amount ? minCoins : -1;
            coinsRequired.push_back(minCoins);
        }

        return coinsRequired.back();        
    }
};