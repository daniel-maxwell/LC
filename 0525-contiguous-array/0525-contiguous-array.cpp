const auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        if (nums.size() == 1) return 0;
        unordered_map<int, int> diffs;
        int oneCount = 0, zeroCount = 0, result = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) ++oneCount;
            else ++zeroCount;

            if (!diffs.contains(oneCount - zeroCount)) {
                diffs[oneCount - zeroCount] = i;
            }
            
            if (oneCount == zeroCount) {
                result = oneCount + zeroCount;
            } else {
                if (diffs.contains(oneCount - zeroCount)) {
                    result = max(result, i - diffs[oneCount - zeroCount]);
                }
            }
        }
        return result;
    }
};