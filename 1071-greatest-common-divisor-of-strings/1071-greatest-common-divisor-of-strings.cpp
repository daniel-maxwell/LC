static const bool a() {
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    string gcdOfStrings(const string str1, const string str2) {
        const string* longStr = str1.length() >= str2.length() ? &str1 : &str2;
        const string* shortStr = str1.length() < str2.length() ? &str1 : &str2;
        string str = *shortStr;
        while (str.length() > 0) {
            cout << str << endl;
            const int sizeL = longStr->length();
            const int sizeS = shortStr->length();
            const int sizeC = str.length();
            if (sizeL % sizeC == 0 && sizeS % sizeC == 0) {
                if (checkSubstr(longStr, shortStr, str)) {
                    return str;
                }
            }
            str.pop_back();
        }
        return "";
    }

    bool checkSubstr(const string* longStr, const string* shortStr, const string strToCheck) {
        const int sizeL = longStr->length();
        const int sizeS = shortStr->length();
        const int sizeC = strToCheck.length();
        for (int i = 0; i < sizeL; i += sizeC) {
            const bool validS = 
                i + sizeC > sizeS || 
                strToCheck == shortStr->substr(i, sizeC) 
            ? true : false;
            const bool validL = strToCheck == longStr->substr(i, sizeC);
            if (!validS || !validL) return false;
        }
        return true;
    }
};