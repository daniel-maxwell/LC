class MyLinkedList {
public:
  struct ListNode {
    int val;
    ListNode *prev;
    ListNode *next;
    ListNode(int val, ListNode *prev = nullptr, ListNode *next = nullptr)
        : val(val), prev(prev), next(next) {}
  };

  MyLinkedList() {
    head = new ListNode(-1);
    tail = new ListNode(-1);
    head->next = tail;
    tail->prev = head;
    length = 0;
  }

  int get(int index) {
    if (index >= length) {
      return -1;
    }
    ListNode *curNode;
    if (index < length / 2) {
      int curIdx = 0;
      curNode = head->next;
      while (curIdx < index) {
        curNode = curNode->next;
        curIdx++;
      }
    } else {
      int curIdx = length - 1;
      curNode = tail->prev;
      while (curIdx > index) {
        curNode = curNode->prev;
        curIdx--;
      }
    }
    return curNode->val;
  }

  void addAtHead(int val) {
    ListNode *newNode = new ListNode(val, head, head->next);
    head->next->prev = newNode;
    head->next = newNode;
    length++;
  }

  void addAtTail(int val) {
    ListNode *newNode = new ListNode(val, tail->prev, tail);
    tail->prev->next = newNode;
    tail->prev = newNode;
    length++;
  }

  void addAtIndex(int index, int val) {
    if (index > length) {
      return;
    } else if (index == 0) {
      addAtHead(val);
      return;
    } else if (index == length) {
      addAtTail(val);
      return;
    }
    ListNode *curNode;
    if (index < length / 2) {
      int curIdx = 0;
      curNode = head->next;
      while (curIdx < index) {
        curNode = curNode->next;
        curIdx++;
      }
    } else {
      int curIdx = length - 1;
      curNode = tail->prev;
      while (curIdx > index) {
        curNode = curNode->prev;
        curIdx--;
      }
    }
    ListNode *newNode = new ListNode(val, curNode->prev, curNode);
    curNode->prev->next = newNode;
    curNode->prev = newNode;
    length++;
    return;
  }

  void deleteAtIndex(int index) {
    if (index >= length) {
      return;
    }
    ListNode *curNode;
    if (index < length / 2) {
      int curIdx = 0;
      curNode = head->next;
      while (curIdx < index) {
        curNode = curNode->next;
        curIdx++;
      }
    } else {
      int curIdx = length - 1;
      curNode = tail->prev;
      while (curIdx > index) {
        curNode = curNode->prev;
        curIdx--;
      }
    }
    curNode->prev->next = curNode->next;
    curNode->next->prev = curNode->prev;
    delete curNode;
    curNode = nullptr;
    length--;
    return;
  }

  ~MyLinkedList() {
    ListNode *curNode = head->next;
    while (curNode != nullptr) {
      ListNode *nextNode = curNode->next;
      delete curNode;
      curNode = nextNode;
    }
  }

private:
  ListNode *head;
  ListNode *tail;
  int length;
};