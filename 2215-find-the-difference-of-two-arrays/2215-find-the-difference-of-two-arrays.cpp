class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int>set1(nums1.begin(), nums1.end());
        unordered_set<int>set2{};
        unordered_set<int>intersection{};
        for (int i = 0; i < nums2.size(); ++i) {
            if (set1.find(nums2[i]) == set1.end()) {
                if (intersection.find(nums2[i]) == intersection.end()) {
                    set2.insert(nums2[i]);
                };
            }
            else {
                set1.erase(nums2[i]);
                intersection.insert(nums2[i]);
            };
        };
        return { {set1.begin(), set1.end()}, {set2.begin(), set2.end()} }; 
    };
};