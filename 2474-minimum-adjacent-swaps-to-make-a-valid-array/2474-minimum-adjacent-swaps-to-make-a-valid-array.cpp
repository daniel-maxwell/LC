class Solution {
public:
    int minimumSwaps(vector<int>& nums) {

        int smallest = nums[0];
        int smallestIdx;
        int largest = nums[0];

        for (const int &n : nums) {
            smallest = min(smallest, n);
            largest = max(largest, n);
        }

        int result = 0;

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == smallest) {
                result += i;
                smallestIdx = i;
                break;
            }
        }

        for (int i = nums.size() - 1; i >= 0; --i) {
            if (nums[i] == largest) {
                result += nums.size() - i - 1;
                result = i < smallestIdx ? result - 1 : result;
                break;
            }
        }

        return result;
    }
};