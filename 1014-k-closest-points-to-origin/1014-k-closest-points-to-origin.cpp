class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<pair<double, vector<int>>> pointsHeap;
        for (const vector<int> &point : points) {
            pointsHeap.push_back(pair<double, vector<int>>{-getEuclidianDist(point[0], point[1]), point});
        }

        make_heap(pointsHeap.begin(), pointsHeap.end());

        vector<vector<int>> result;

        while (k > 0) {
            pop_heap(pointsHeap.begin(), pointsHeap.end());
            result.push_back(pointsHeap.back().second);
            pointsHeap.pop_back();
            --k;
        }

        return result;
    }

    double getEuclidianDist(int x, int y) {
        return sqrt(double(pow(x, 2)) + double(pow(y, 2)));
    }
};