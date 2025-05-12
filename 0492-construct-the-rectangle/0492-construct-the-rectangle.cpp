class Solution {
public:
    vector<int> constructRectangle(int area) {
        vector<int> result {area, 1};
        int minDiff = area - 1;

        for (int i = 1; i <= area / 2; ++i) {
            if (area % i == 0 && abs((area / i) - i) <= minDiff) {
                result[0] = area / i;
                result[1] = i;
                minDiff = abs((area / i) - i);
            }
        }

        return result[0] >= result[1] ? result : vector<int>{result[1], result[0]};
    }
};