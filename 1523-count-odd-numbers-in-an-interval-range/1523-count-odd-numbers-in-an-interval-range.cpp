class Solution {
public:
    int countOdds(int low, int high) {
        low -= low % 2;
        high += high % 2;
        return floor((high - low) / 2);
    };
};