class Solution {
public:
    int tribonacci(int n) {
        vector<int>trib {0, 1, 1};
        for (int i = 3; i <= n; ++i) {
            int len = trib.size();
            trib.push_back(trib[len-1] + trib[len-2] + trib[len-3]);
        }
        return trib[n];
    }
};