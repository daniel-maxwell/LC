/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {

        unordered_map<int, vector<ListNode*>> valToNodes;
        vector<int> sortedVals;

        for (ListNode* &head : lists) {
            if (head == nullptr) continue;
            ListNode* cur = head;
            while (cur != nullptr) {
                cout << cur->val << ", ";
                sortedVals.push_back(cur->val);
                valToNodes[cur->val].push_back(cur);
                cur = cur->next;
            }
        }

        if (sortedVals.empty()) return nullptr;
        sort(sortedVals.begin(), sortedVals.end());
        ListNode* head = valToNodes[sortedVals[0]][0];

        ListNode* cur = head;

        for (int i = 1; i < valToNodes[sortedVals[0]].size(); ++i) {
            ListNode* next = valToNodes[sortedVals[0]][i];
            cur->next = next;
            cur = cur->next;
        }

        int i = valToNodes[sortedVals[0]].size();
        cur = valToNodes[sortedVals[0]].back();
        
        while (i < sortedVals.size()) {
            for (ListNode* node : valToNodes[sortedVals[i]]) {
                cur->next = node;
                cur = cur->next;
            }
            i += valToNodes[sortedVals[i]].size();
        }

        return head;        
    }
};