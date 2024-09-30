static const bool a() {
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    int minOperations(vector<int>& nums) {
            unordered_map<int, int> count;
            
            // Count occurrences of each number
            for (int num : nums) {
                ++count[num];
            }
            
            int result = 0;
            
            // Calculate minimum operations
            for (auto& pair : count) {
                int c = pair.second; // c is the count of the current number
                
                if (c == 1) {
                    return -1; // If any number appears exactly once, return -1
                }
                
                // Calculate number of operations needed
                result += ceil(static_cast<double>(c) / 3);
            }
            
            return result;
    }
};