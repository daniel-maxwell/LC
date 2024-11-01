auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 'c';
}();
class Solution {
public:
    int minimumLength(string s) {
        deque<char> deq;
        for (const char &c : s) deq.push_back(c);
        char cur = deq.front();
        while (deq.size() >= 2 && (
            (cur == deq.front() && cur == deq.back()) ||
                deq.front() == deq.back())
            ) {
            if (cur != deq.front()) {
                cur = deq.front();
                continue;
            } else {
                while (!deq.empty() && cur == deq.front()) deq.pop_front();
                while (!deq.empty() && cur == deq.back()) deq.pop_back();
            }
        }
        return deq.size();
    }
};