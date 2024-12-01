static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}();
class Solution {
public:
    int minSwaps(vector<int>& data) {
        int oneCountTotal = 0;

        for (const int &n : data) {
            if (n == 1) {
                ++oneCountTotal;
            }
        }

        int l = 0, r = 0, currOneCount = 0;

        while (r < oneCountTotal) {
            if (data[r] == 1) {
                ++currOneCount;
            }
            ++r;
        }

        int result = (r - l) - currOneCount;

        while (r < data.size()) {
            if (data[l] == 1) {
                --currOneCount;
            }
            ++l;
            if (data[r] == 1) {
                ++currOneCount;
            }
            ++r;
            result = min(result, (r - l) - currOneCount);
        }

        return result;
    }
};