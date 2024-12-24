class Solution {
public:
    vector<int> goodDaysToRobBank(vector<int>& security, int time) {

        vector<bool> nonDecreasingWindow(security.size(), false);
        int ptr = security.size() - 2;
        bool isNonDecreasing;
        int windowSize = 1;
        while (ptr >= 0) {
            if (security[ptr] > security[ptr+1]) {
                windowSize = 0;
            }
            if (windowSize >= time) {
                isNonDecreasing = true;
            } else {
                isNonDecreasing = false;
            }
            nonDecreasingWindow[ptr] = isNonDecreasing;
            ++windowSize;
            --ptr;
        }

        vector<int> result;
        if (time == 0) {
            nonDecreasingWindow.back() = true;
            result.push_back(0);   
        }

        windowSize = 1;
        ptr = 1;
        bool isNonIncreasing = true;
        int length = security.size() - time;
        while (ptr < length) {
            if (security[ptr] > security[ptr-1]) {
                windowSize = 0;
            }
            if (windowSize >= time) {
                isNonIncreasing = true;
            } else {
                isNonIncreasing = false;
            }
            if (isNonIncreasing && nonDecreasingWindow[ptr]) {
                result.push_back(ptr);
            }
            ++windowSize;
            ++ptr;
        }

        return result;        
    }
};