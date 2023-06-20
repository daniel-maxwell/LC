class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res(nums1.size(), -1);
        stack<int> s;
        map<int, int> nums1Idx;
        for (size_t i = 0; i < nums1.size(); ++i) nums1Idx[nums1[i]] = i;

        for (int i = 0; i < nums2.size(); ++i) {
            int curr = nums2[i];
            while ((!s.empty()) && curr > s.top()) {
                res[nums1Idx[s.top()]] = curr;
                s.pop();
            };
            if (nums1Idx.find(curr) != nums1Idx.end()) s.push(curr);
        };
        return res;
    };
};