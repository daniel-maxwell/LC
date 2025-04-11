class Solution {
public:
    const vector<int> relativeSortArray(const vector<int>& arr1, const vector<int>& arr2) {
        
        unordered_map<int, int> ordering;
        unordered_set<int> arr2Set(arr2.begin(), arr2.end());
        unordered_map<int, int> counts;

        for (int i = 0; i < arr2.size(); ++i) {
            ordering[i] = arr2[i];
        }

        for (const int &n : arr1) {
            ++counts[n];
        }

        vector<int> result;

        int i = 0;

        while (ordering.contains(i)) {
            for (int j = 0; j < counts[ordering[i]]; ++j) {
                result.push_back(ordering[i]);
            }
            ++i;
        }

        vector<int> resultPostfix;

        for (const int &n : arr1) {
            if (!arr2Set.contains(n)) {
                resultPostfix.push_back(n);
            }
        }

        sort(resultPostfix.begin(), resultPostfix.end());
        result.insert(result.end(), resultPostfix.begin(), resultPostfix.end());

        return result;
    }
};