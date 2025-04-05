/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* createBinaryTree(const vector<vector<int>>& descriptions) {

        unordered_set<int> potentialRoots;

        for (const vector<int> &d : descriptions) {
            if (!treeMap.contains(d[0])) {
                treeMap[d[0]] = pair<int, int> {0, 0};
            }
            if (d[2] == 1) treeMap[d[0]].first = d[1];
            else treeMap[d[0]].second = d[1];
            potentialRoots.insert(d[0]);
        }

        for (const vector<int> &d : descriptions) {
            potentialRoots.erase(d[1]);
        }

        int root = vector<int>(potentialRoots.begin(), potentialRoots.end())[0];

        TreeNode* rootNode = new TreeNode(root);
        createTree(rootNode);

        return rootNode;
    }

private:
    unordered_map<int, pair<int, int>> treeMap;
    
    void createTree(TreeNode* root) {
        int leftVal = treeMap[root->val].first;
        int rightVal = treeMap[root->val].second;

        if (leftVal != 0) {
            root->left = new TreeNode(leftVal);
            createTree(root->left);
        }

        if (rightVal != 0) {
            root->right = new TreeNode(rightVal);
            createTree(root->right);
        }
    }
};