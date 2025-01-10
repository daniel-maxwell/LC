class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        if (k >= arr[0]) k -= (arr[0] - 1);
        else return k;
        int i = 0;
        while (i < arr.size() - 1 && k > 0) {
            const int numMissing = arr[i+1] - arr[i] - 1;
            if (k - numMissing > 0) k -= numMissing;
            else return arr[i] + k;
            ++i;
        }
        return arr[arr.size() - 1] + k;
    }
};