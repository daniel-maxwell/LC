static const bool a() {
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    string largestGoodInteger(string num) {
        int result = -1;
        for (int i = 2; i < num.size(); ++i) {
            if (num[i] == num[i-1] && num[i] == num[i-2]) {
                string str(1, num[i]);
                str += num[i-1]; str += num[i-2];
                result = max(result, std::stoi(str));
            }
        }
        if (result == -1) return "";
        return result == 0 ? "000" : std::to_string(result);
    }
};