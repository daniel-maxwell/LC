class Solution {
public:
    string reorganizeString(string s) {

        unordered_map<char, int> charCounts;

        for (const char &c : s) { 
            ++charCounts[c];
            if (charCounts[c] > (s.size() + 1) / 2) {
                return "";
            }
        }

        priority_queue<pair<int, char>> pq;

        for (const pair<char, int> &entry : charCounts) {
            pq.push(pair<int, char>{entry.second, entry.first});
        }

        string result = "";

        while (!pq.empty()) {
            if (result.size() == 0 || result.back() != pq.top().second) {
                pair<int, char> top = pq.top();
                pq.pop();
                --top.first;
                if (top.first > 0) {
                    pq.push(top);
                }
                result += top.second;
            } else {
                pair<int, char> top = pq.top();
                pq.pop();
                pair<int, char> second = pq.top();
                pq.pop();
                --second.first;
                if (second.first > 0) {
                    pq.push(second);
                }
                result += second.second;
                pq.push(top);
            }
        }

        return result;
    }
};