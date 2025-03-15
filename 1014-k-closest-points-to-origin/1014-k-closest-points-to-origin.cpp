class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {

        vector<pair<double, int>> pointsHeap;

        for (int i = 0; i < points.size(); ++i) {
            const pair<double, int> dist {
                calcDistance(points[i][0], points[i][1], 0, 0), i
            };
            pointsHeap.push_back(dist);
            push_heap(pointsHeap.begin(), pointsHeap.end());
        }

        vector<vector<int>> result;

        for (int i = 0; i < k; ++i) {
            pop_heap(pointsHeap.begin(), pointsHeap.end());
            const vector<int> point = points[pointsHeap.back().second];
            result.push_back(point);
            pointsHeap.pop_back();
        }

        return result;
    }

    const double calcDistance(int x1, int y1, int x2, int y2) {
        return -sqrt(pow(double(x1) - double(x2), 2) + pow(double(y1) - double(y2), 2));
    }
};