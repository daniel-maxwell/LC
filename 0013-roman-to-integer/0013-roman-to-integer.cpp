class Solution {
public:
    int romanToInt(string s) {

        int res = 0;

        unordered_map<char, int> roman = {
            {'M' , 1000},
            {'D' , 500},
            {'C' , 100},
            {'L' , 50},
            {'X' , 10},
            {'V' , 5},
            {'I' , 1}
        };

        int prevNum = 0;

        for (int i = s.size() - 1; i >= 0; --i) {
            int currNum = roman[s[i]];
            if (currNum < prevNum) res -= currNum;
            else res += currNum;
            prevNum = currNum;
        };
        return res;
    };
};