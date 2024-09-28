static const bool a() {
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    string largestNumber(const vector<int>& nums) {
        int greatest = 0;
        std::vector<std::string> strNums(nums.size(), "");
        for (int i = 0; i < nums.size(); ++i) {
            strNums[i] = std::to_string(nums[i]);
            if (nums[i] > greatest) greatest = nums[i];
        }
        if (greatest == 0) return "0";
        std::sort(strNums.begin(), strNums.end(), [](std::string a, std::string b) {
                return a + b >= b + a;
            }
        );
        std::stringstream resultStream;
        for (const std::string& str : strNums) resultStream << str;
        return resultStream.str();
    }
};