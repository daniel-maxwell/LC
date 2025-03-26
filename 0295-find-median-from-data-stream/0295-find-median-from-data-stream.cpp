class MedianFinder {
public:
    MedianFinder() {
        minHeapSize = 0;
        maxHeapSize = 0;
    }
    
    void addNum(int num) {
        if (maxHeap.empty() || num <= maxHeap.front()) {
            maxHeap.push_back(num);
            push_heap(maxHeap.begin(), maxHeap.end());
        } else {
            minHeap.push_back(-num);
            push_heap(minHeap.begin(), minHeap.end());
        }
        rebalanceHeaps();
    }
    
    double findMedian() {
        if (maxHeapSize > minHeapSize) {
            return double(maxHeap.front());
        } else if (maxHeapSize < minHeapSize) {
            return double(-minHeap.front());
        } else {
            return (double(maxHeap.front()) + double(-minHeap.front())) / double(2);
        }
    }

    void rebalanceHeaps() {
        if (!(maxHeap.size() == minHeap.size() || 
            abs(int(maxHeap.size() - minHeap.size())) == 1)) {
            if (maxHeap.size() > minHeap.size()) {
                pop_heap(maxHeap.begin(), maxHeap.end());
                const int cur = maxHeap.back();
                maxHeap.pop_back();
                minHeap.push_back(-cur);
                push_heap(minHeap.begin(), minHeap.end());
            } else {
                pop_heap(minHeap.begin(), minHeap.end());
                const int cur = minHeap.back();
                minHeap.pop_back();
                maxHeap.push_back(-cur);
                push_heap(maxHeap.begin(), maxHeap.end());
            }
        }
        minHeapSize = minHeap.size();
        maxHeapSize = maxHeap.size();
    }

    vector<int> minHeap; // will use negative numbers
    int minHeapSize;
    vector<int> maxHeap;
    int maxHeapSize;
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */


 /*
- you have a min heap and a max heap.
- size of each heap should be different by at most one.
- finding a median is the process of simply peeking either heap (if uneven) else taking the mean of the top of both heaps.


- max contains smaller half, min contains larger half
- 

 */