class Solution {
public:
    const bool isRectangleOverlap(const vector<int>& rec1, const vector<int>& rec2) {
        const int minX1 = min(rec1[0], rec1[2]), maxX1 = max(rec1[0], rec1[2]);
        const int minX2 = min(rec2[0], rec2[2]), maxX2 = max(rec2[0], rec2[2]);
        const bool overLapsX = (minX1 >= minX2 && minX1 < maxX2) || (minX2 >= minX1 && minX2 < maxX1); 
        const int minY1 = min(rec1[1], rec1[3]), maxY1 = max(rec1[1], rec1[3]);
        const int minY2 = min(rec2[1], rec2[3]), maxY2 = max(rec2[1], rec2[3]);
        const bool overLapsY = (minY1 >= minY2 && minY1 < maxY2) || (minY2 >= minY1 && minY2 < maxY1);
        return overLapsX && overLapsY; 
    }
};