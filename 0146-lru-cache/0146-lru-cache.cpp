class LRUCache {
public:
    // Doubly linked list
    struct ListNode { 
        int key;
        int val;
        ListNode* prev;
        ListNode* next;
        ListNode() : key(0), val(0), prev(nullptr), next(nullptr) {}
        ListNode(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
        ListNode(int k, int v, ListNode* p, ListNode* n) : key(k), val(v), prev(p), next(n) {}
    };

    // Dummy head and tail nodes
    ListNode head = ListNode();
    ListNode tail = ListNode();

    unordered_map<int, ListNode*> keyMap;
    int remainingCapacity;

    LRUCache(int capacity) {
        head.next = &tail;
        tail.prev = &head;
        remainingCapacity = capacity;
    }
    
    int get(int key) {
        if (!keyMap.contains(key)) {
            return -1;
        }
        removeNode(keyMap[key]);
        insertAtFront(keyMap[key]);
        return keyMap[key]->val;
    }
    
    void put(int key, int value) {
        if (keyMap.contains(key)) {
            keyMap[key]->val = value;
            removeNode(keyMap[key]);
            insertAtFront(keyMap[key]);
        } else {
            if (remainingCapacity == 0) {
                evictLRUNode();
            } else {
                --remainingCapacity;
            }
            ListNode* newNode = new ListNode(key, value);
            keyMap[key] = newNode;
            insertAtFront(keyMap[key]);
        }
    }

    void insertAtFront(ListNode* nodePtr) {
        nodePtr->next = head.next;
        nodePtr->prev = &head;
        head.next->prev = nodePtr;
        head.next = nodePtr;
    }

    void evictLRUNode() {
        ListNode* node = tail.prev;
        removeNode(node);
        keyMap.erase(node->key);
        delete node;
    }

    void removeNode(ListNode* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */