/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        
        mapParents(root);
        
        unordered_set<int> visited;
        queue<TreeNode*> q;
        q.push(target);

        vector<int> result;

        while (k > 0) {
            int length = q.size();
            while (length > 0) {
                TreeNode* cur = q.front();
                q.pop();
                if (parentMap.contains(cur->val) && !visited.contains(cur->val)) {
                    q.push(parentMap[cur->val]);
                    visited.insert(cur->val);
                } 
                if (cur->left != nullptr && !visited.contains(cur->left->val)) {
                    q.push(cur->left);
                    visited.insert(cur->left->val);
                }
                if (cur->right != nullptr && !visited.contains(cur->right->val)) {
                    q.push(cur->right);
                    visited.insert(cur->right->val);
                } 
                visited.insert(cur->val);
                --length;
            }
            --k;
        }

        while (!q.empty()) {
            result.push_back(q.front()->val);
            q.pop();
        }

        return result;
    }

    void mapParents(TreeNode* root) {
        if (root == nullptr) return;
        if (root->left != nullptr) {
            parentMap[root->left->val] = root;
        }
        if (root->right != nullptr) {
            parentMap[root->right->val] = root;
        }
        mapParents(root->left);
        mapParents(root->right);
    }

    unordered_map<int, TreeNode*> parentMap;
};