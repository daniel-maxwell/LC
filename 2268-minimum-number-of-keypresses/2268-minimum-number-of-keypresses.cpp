static const bool Init() {
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    const int minimumKeypresses(const string &s) {
        vector<int> charCounts(26, 0);

        for (const char &c : s) {
            ++charCounts[c - 'a'];
        }

        sort(charCounts.begin(), charCounts.end(), greater<int>());

        int button = 1, layerCount = 1, keyPresses = 0;        
        for (int i = 0; i < 26; ++i) {
            if (charCounts[i] == 0) break;
            if (button == 10) {
                button = 1;
                ++layerCount;
            }
            keyPresses += charCounts[i] * layerCount;
            ++button;
        }

        return keyPresses;
    }
};