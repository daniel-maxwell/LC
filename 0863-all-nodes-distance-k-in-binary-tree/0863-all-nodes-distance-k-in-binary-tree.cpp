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
        dfs(root);
        set<int> visited {target->val};
        queue<TreeNode*>q;
        q.push(target);

        while (!q.empty() && k > 0) {
            const int length = q.size();
            for (int _ = 0; _ < length; ++_) {
                TreeNode* cur = q.front();
                q.pop();
                const vector<TreeNode*> &neighbours = neighbourMap[cur];
                for (int i = 0; i < neighbours.size(); ++i) {
                    if (!visited.contains(neighbours[i]->val)) {
                        q.push(neighbours[i]);
                    }
                }
                visited.insert(cur->val);
            }
            --k;
        }

        vector<int> result;
        while (!q.empty()) {
            result.push_back(q.front()->val);
            q.pop();
        }
        return result;
    }

private:
    void dfs(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        if (root->left != nullptr) {
            neighbourMap[root->left].push_back(root);
            neighbourMap[root].push_back(root->left);
            dfs(root->left);
        }
        if (root->right != nullptr) {
            neighbourMap[root->right].push_back(root);
            neighbourMap[root].push_back(root->right);
            dfs(root->right);
        }
        return;
    }

    unordered_map<TreeNode*, vector<TreeNode*>> neighbourMap;
};