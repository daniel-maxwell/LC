class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        unordered_map<int, int> numCounts;
        int l = 0, r = 0;

        while (r < k) {
            heap.push_back(nums[r]);
            ++numCounts[nums[r]];
            ++r;
        }

        make_heap(heap.begin(), heap.end());
        vector<int> result {heap.front()};

        while (r < nums.size()) {
            if ((!numCounts.contains(nums[r])) || numCounts[nums[r]] == 0) {
                pushToHeap(nums[r]);
            }
            ++numCounts[nums[r]];
            --numCounts[nums[l]];
            while (numCounts[heap.front()] == 0) popFromHeap();
            result.push_back(heap.front());
            ++r;
            ++l;
        }
        return result;
    }

private:
    vector<int> heap;

    void pushToHeap(const int &n) {
        heap.push_back(n);
        push_heap(heap.begin(), heap.end());
        return;
    }

    void popFromHeap() {
        pop_heap(heap.begin(), heap.end());
        heap.pop_back();
        return;
    }
};