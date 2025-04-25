class Solution {
public:
    int maxNumberOfApples(vector<int>& weight) {
        sort(weight.begin(), weight.end());

        int cap = 5000;
        int result = 0;

        for (const int &w : weight) {
            if (cap - w < 0) {
                return result;
            }
            cap -= w;
            ++result;
        }

        return result;
    }
};