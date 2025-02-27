class Solution {
public:
    int compress(vector<char>& chars) {
        int i = 0;
        while (i < chars.size()) {
            const char curr = chars[i];
            int size = 1;
            for (int j = i + 1; j < chars.size(); ++j) {
                if (chars[j] != curr) break;
                ++size;
            }
            if (size > 1) {
                const string compressed = curr + to_string(size);
                const int cSize = compressed.size();
                const int start = i + size - cSize;
                const int end = i + size;
                int l = 0;
                for (int k = start; k < end; ++k) {
                    chars[k] = compressed[l];
                    ++l;
                }
                chars.erase(chars.begin() + i, chars.begin() + start);
                i += cSize;
            } else {
                chars[i + size - 1] = curr;
                chars.erase(chars.begin() + i, chars.begin() + i + size - 1);
                ++i;
            }
        }
        return chars.size();
    }
};