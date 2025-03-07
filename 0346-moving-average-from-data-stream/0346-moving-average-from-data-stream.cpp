class MovingAverage {
public:
    MovingAverage(int size) {
        windowSize = size;
    }
    
    const double next(int val) {
        if (q.size() == windowSize) {
            sum -= q.front();
            q.pop();
        }
        q.push(val);
        sum += val;
        double avg = double(sum) / double(q.size());
        return avg;
    }

    queue<int> q {};
    int sum = 0;
    int windowSize;
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */