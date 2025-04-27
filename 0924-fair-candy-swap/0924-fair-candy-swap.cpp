class Solution {
public:
    vector<int> fairCandySwap(vector<int>& aliceSizes, vector<int>& bobSizes) {
        int sumA = 0, sumB = 0;
        for (int x : aliceSizes) sumA += x;
        for (int y : bobSizes) sumB += y;

        int delta = (sumA - sumB) / 2;

        unordered_set<int> bobSet(bobSizes.begin(), bobSizes.end());
        for (int x : aliceSizes) {
            int y = x - delta;
            if (bobSet.count(y)) {
                return {x, y};
            }
        }
        return {};
    }
};
