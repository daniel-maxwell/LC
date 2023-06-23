class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> ans;
        
        for(int x : nums){
            int currentVal = abs(x);
            nums[currentVal-1] = 0 - abs(nums[currentVal-1]);
        }
        
        for(int i = 1; i <= nums.size(); i++)
            if(nums[i-1] > 0) ans.push_back(i);
        
        return ans;
    }
};