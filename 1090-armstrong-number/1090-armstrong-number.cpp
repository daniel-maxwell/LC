class Solution {
public:
    const bool isArmstrong(const int n) {
        const int k = to_string(n).size();
        int nCopy = n, sum = 0;
        while (nCopy > 0) {
            sum += pow(nCopy % 10, k);
            nCopy /= 10;
        }
        return sum == n;
    }
};