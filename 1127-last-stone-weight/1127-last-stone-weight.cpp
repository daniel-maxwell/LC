class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        vector<int> stonesHeap;
        for (const int &n : stones) {
            stonesHeap.push_back(n);
        }
        make_heap(stonesHeap.begin(), stonesHeap.end());
        while (!stonesHeap.empty()) {
            pop_heap(stonesHeap.begin(), stonesHeap.end());
            int stone1 = stonesHeap.back();
            stonesHeap.pop_back();
            if (!stonesHeap.empty()) {
                pop_heap(stonesHeap.begin(), stonesHeap.end());
                int stone2 = stonesHeap.back();
                stonesHeap.pop_back();
                int resultStone = max(stone1, stone2) - min(stone1, stone2);
                if (resultStone > 0) {
                    stonesHeap.push_back(resultStone);
                    push_heap(stonesHeap.begin(), stonesHeap.end());
                }
            } else {
                return stone1;
            }
        }
        return 0;
    }
};