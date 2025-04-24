class Solution {
public:
    const vector<string> findWords(const vector<string>& words) {
        const unordered_map<int, char> mapping {
            {'q', 1},
            {'w', 1},
            {'e', 1},
            {'r', 1},
            {'t', 1},
            {'y', 1},
            {'u', 1},
            {'i', 1},
            {'o', 1},
            {'p', 1},
            {'q', 1},
            {'w', 1},
            {'e', 1},
            {'r', 1},
            {'t', 1},
            {'y', 1},
            {'u', 1},
            {'i', 1},
            {'o', 1},
            {'p', 1},
            {'a', 2},
            {'s', 2},
            {'d', 2},
            {'f', 2},
            {'g', 2},
            {'h', 2},
            {'j', 2},
            {'k', 2},
            {'l', 2},
            {'z', 3},
            {'x', 3},
            {'c', 3},
            {'v', 3},
            {'b', 3},
            {'n', 3},
            {'m', 3}
        };

        vector<string> result;

        for (const string &s : words) {
            int level = -1;
            int valid = true;
            for (const char &c : s) {
                if (level == -1) {
                    level = mapping.at(tolower(c));
                } else {
                    if (mapping.at(tolower(c)) != level) {
                        valid = false;
                        break;
                    }
                }
            }
            if (valid) {
                result.push_back(s);
            }
        }

        return result;
    }
};