class Solution {
public:
    const int minMeetingRooms(vector<vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end());
        std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
        minHeap.push(0);
        for (const vector<int> &meeting : intervals) {
            if (minHeap.top() <= meeting[0]) {
                minHeap.pop();
            }
            minHeap.push(meeting[1]);
        }
        return minHeap.size();
    }
};