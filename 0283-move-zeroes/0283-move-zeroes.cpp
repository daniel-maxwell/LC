class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i=0, j=0;
        while (i + j < nums.size()){
            if (nums[i] == 0) {
                nums.erase(nums.begin()+i);
                nums.push_back(0);
                ++j;
            }
            else ++i;
        };
    };
};