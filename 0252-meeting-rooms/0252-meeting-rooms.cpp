static const bool Init() {
    std::ios_base::sync_with_stdio(false), std::cout.tie(nullptr), std::cin.tie(nullptr);
    return true;
}
class Solution {
public:
    static const bool canAttendMeetings(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int maxEnd = 0;
        for (const vector<int> &meeting : intervals) {
            if (maxEnd > meeting[0]) return false;
            maxEnd = max(maxEnd, meeting[1]);
        }
        return true;
    }
};