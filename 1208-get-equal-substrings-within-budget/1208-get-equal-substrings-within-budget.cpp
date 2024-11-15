static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    const int equalSubstring(const string &s, const string &t, const int maxCost) {
        int l = 0, r = 0;
        int budget = maxCost, result = 0;
        while (r < s.size()) {
            int cost = getCost(s[r], t[r]);
            if (budget >= cost) {
                budget -= cost;
                result = max(result, r - l + 1);
                ++r;
            } else {
                if (l == r) {
                    ++l;
                    ++r;
                    continue;
                }
                budget += getCost(s[l], t[l]);
                ++l;
            }
        }
        return result;
    }

    const int getCost(const char &a, const char &b) {
        int costA = a - 'a', costB = b - 'a';
        return abs(costA - costB);
    }
};