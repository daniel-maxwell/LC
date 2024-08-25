class Solution {
public:
    int getSum(int a, int b) {
        vector<int> sumVec {a, b};
        return accumulate(sumVec.begin(), sumVec.end(), 0);
    }
};