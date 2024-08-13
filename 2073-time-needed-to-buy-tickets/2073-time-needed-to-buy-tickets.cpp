class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        deque<int> q = {};
        q.insert(q.end(), tickets.begin(), tickets.end());
        uint16_t timeEllapsed = 0;
        uint8_t kPos = k;
        while (!q.empty()) {
            uint8_t customer = q.front();
            q.pop_front();
            customer--;
            timeEllapsed++;
            if (customer > 0) {
                q.push_back(customer);
                if (kPos == 0) {
                    kPos = q.size();
                }
            } else {
                if (kPos == 0) {
                    return timeEllapsed;
                }
            }
            kPos--;
        }
        return -1;
    }
};