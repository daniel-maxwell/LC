class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int currMax = arr[arr.size() - 1];
        for (int i = arr.size() - 2; i > -1; --i) {
            if (arr[i] > currMax) {
                int prevMax = currMax;
                currMax = arr[i];
                arr[i] = prevMax;
            }
            else arr[i] = currMax;
        }
        arr[arr.size() - 1] = -1;
        return arr;
    }
};