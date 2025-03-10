class Logger {
public:
    Logger() {
    }
    
    const bool shouldPrintMessage(const int timestamp, const string message) {
        bool result = false;
        if (!messages.contains(message) || timestamp >= messages[message] + 10) {
            result = true;
            messages[message] = timestamp;
        }
        return result;
    }
    unordered_map<string, int> messages;
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */