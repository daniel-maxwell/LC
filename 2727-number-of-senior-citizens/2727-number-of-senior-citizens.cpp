class Solution {
public:
    int countSeniors(vector<string>& details) {
        int result = 0;

        for (const string &s : details) {
            const string age = s.substr(11, 2);
            if (stoi(age) > 60) ++result;
        }
        
        return result;
    }
};