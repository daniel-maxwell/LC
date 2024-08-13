class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        queue<int> q = {};
        for (int ticket : tickets) {
            q.push(ticket);
        }
        uint16_t timeEllapsed = 0;
        uint8_t kPos = k;
        while (!q.empty()) {
            uint8_t customer = q.front();
            q.pop();
            customer--;
            timeEllapsed++;
            if (customer > 0) {
                q.push(customer);
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