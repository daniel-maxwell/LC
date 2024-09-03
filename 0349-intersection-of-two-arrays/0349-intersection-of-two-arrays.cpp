class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> numSet;
        for (int v : nums1) numSet.insert(v);
        vector<int> res;
        int prev = -1;
        sort(nums2.begin(), nums2.end());
        for (int i = 0; i < nums2.size(); ++i) {
            if (nums2[i] == prev) {
                continue;
            }
            if (numSet.contains(nums2[i])) {
                res.push_back(nums2[i]);
            }
            prev = nums2[i];
        }
        return res;
    }
};