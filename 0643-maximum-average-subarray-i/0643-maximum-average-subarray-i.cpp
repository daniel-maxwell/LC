class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int currentSum;
        int i = 0, j = 0;

        while (j < k) {
            currentSum += nums[j];
            ++j;
        }

        double currentAverage = double(currentSum) / k;
        double result = currentAverage;
        
        while (j < nums.size()) {
            currentSum -= nums[i];
            ++i;
            currentSum += nums[j];
            ++j;
            currentAverage = double(currentSum) / k;
            result = max(result, currentAverage);
        }

        return result;
    }
};