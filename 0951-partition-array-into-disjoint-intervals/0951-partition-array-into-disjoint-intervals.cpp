class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {

        vector<int> numsSorted(nums.begin(), nums.end());
        sort(numsSorted.begin(), numsSorted.end());

        unordered_map<int, int> orderToNumber; // Ranking of smallest to largest
        unordered_map<int, int> numberToOrder; // Where each number falls in ranking
        unordered_map<int, int> orderToIndex; // The index of that number in nums

        for (int i = 0; i < numsSorted.size(); ++i) {
            orderToNumber[i] = numsSorted[i];
            numberToOrder[numsSorted[i]] = i;
        }

        for (int i = 0; i < nums.size(); ++i) {
            const int ranking = numberToOrder[nums[i]];
            orderToIndex[ranking] = i;
        }

        int maximumLeft = nums[0];
        int minimumRight = orderToIndex[0] == 0 ? orderToNumber[1] : orderToNumber[0];
        int orderIndex = orderToIndex[0] == 0 ? 1 : 0;

        for (int i = 0; i < nums.size(); ++i) {
            maximumLeft = max(maximumLeft, nums[i]);
            while (orderToIndex[orderIndex] < i + 1) {
                ++orderIndex;
                minimumRight = orderToNumber[orderIndex];
            }
            if (maximumLeft <= minimumRight) {
                return i + 1;
            }
        }

        return 0;
    }
};