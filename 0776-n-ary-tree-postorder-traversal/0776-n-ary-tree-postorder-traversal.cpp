/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    const vector<int> postorder(const Node* root) {
        traverse(root);
        return result;
    }
    void traverse(const Node* root) {
        if (root == nullptr) return;
        for (const auto &node : root->children) traverse(node);
        result.push_back(root->val);
    }
    vector<int> result;
};