class MyHashSet {
public:
    int32_t arrSize;
    vector<bool> storage;
    MyHashSet() : arrSize(pow(10, 6) + 1), storage(arrSize, false) {}
    
    void add(int key) {
        storage[key] = true;
    }
    
    void remove(int key) {
        storage[key] = false;
    }
    
    bool contains(int key) { 
        return storage[key];
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */