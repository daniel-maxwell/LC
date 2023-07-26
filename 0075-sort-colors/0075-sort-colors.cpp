class Solution {
public:
    void sortColors(vector<int>& nums) {
        int r = 0, w = 0, b = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 0) ++r;
            else if (nums[i] == 1) ++w;
            else ++b; 
        };
        nums.erase(nums.begin(), nums.begin() + r);
        nums.insert(nums.begin(), r, 0);
        nums.erase(nums.begin()+r, nums.begin() + r + w);
        nums.insert(nums.begin() + r, w, 1);
        nums.erase(nums.begin() + r + w, nums.end());
        nums.insert(nums.begin() + r + w, b, 2);
    };
};