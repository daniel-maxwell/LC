class Solution {
public:
    const vector<int> anagramMappings(const vector<int>& nums1, const vector<int>& nums2) {
        unordered_map<int, vector<int>> idxMap;

        for (int i = 0; i < nums2.size(); ++i) {
            idxMap[nums2[i]].push_back(i);
        }

        vector<int> result;

        for (const int &n : nums1) {
            result.push_back(idxMap[n].back());
            idxMap[n].pop_back();
        }

        return result;
    }
};