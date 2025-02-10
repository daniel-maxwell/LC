class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        unordered_map<char, int> occ;
        for (const char &c : stones) ++occ[c];
        int result = 0;
        for (const char &c : jewels) result += occ[c];
        return result;
    }
};