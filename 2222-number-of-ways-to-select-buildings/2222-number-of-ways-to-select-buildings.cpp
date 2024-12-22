class Solution {
public:
    long long numberOfWays(string s) {
        int zeroCount = 0, oneCount = 0;

        for (const char &c : s) {
            if (c == '0') ++zeroCount;
            else ++oneCount;
        }

        long long 
            zerosOnRight = zeroCount, 
            zerosOnLeft = 0, 
            onesOnRight = oneCount, 
            onesOnLeft = 0,
            result = 0;

        for (const char &c : s) {
            if (c == '0') {
                result += onesOnLeft * onesOnRight;
                ++zerosOnLeft;
                --zerosOnRight;
            } else {
                result += zerosOnLeft * zerosOnRight;
                ++onesOnLeft;
                --onesOnRight;
            }
        }

        return result;
    }
};