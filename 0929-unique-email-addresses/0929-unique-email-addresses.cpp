class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        set<string> s;
        for (string e : emails) {
            for (int i = 0; i < e.size(); ++i) {

                if (e[i] == '.') e.erase(i, 1);

                else if (e[i] == '+') {
                    while (e[i] != '@') e.erase(i, 1);
                };

                if (e[i] == '@') {
                    s.insert(e);
                    break;
                };
            };
        };
        return s.size();
    };
};