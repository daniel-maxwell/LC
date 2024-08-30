class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int zeroCount = 0;
        int oneCount = 0;
        for (char c : s) {
            if (c == '0') {
                ++zeroCount;
            } else {
                ++oneCount;
            }
        }
        string res(oneCount - 1, '1');
        res.append(zeroCount, '0');
        res.append(1, '1');
        return res;
    }
};