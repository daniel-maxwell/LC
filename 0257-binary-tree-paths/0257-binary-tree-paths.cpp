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
    vector<string> binaryTreePaths(TreeNode* root) {
        return getPaths(root, "");
    }

    vector<string> getPaths(TreeNode* root, string curr) {
        if (root == nullptr) return result;

        const int currLength = curr.size();
        if (currLength == 0) curr += to_string(root->val);
        else curr += "->" + to_string(root->val);

        if (root->left == nullptr && root->right == nullptr) {
            result.push_back(curr);
        } else {
            getPaths(root->left, curr);
            getPaths(root->right, curr);
        }
        curr = curr.substr(0, currLength);

        return result;
    }

    vector<string> result;
};