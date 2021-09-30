// Problem : https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1
class Solution
{
public:
    //Function to find the vertical order traversal of Binary Tree.
    map<int, vector<int>> m;
    void bfs(Node *v)
    {
        queue<pair<Node * , int>> q;
        q.push({v, 0});
        while (!q.empty())
        {
            auto x = q.front();
            q.pop();
            auto u = x.first;
            int t = NULL)
                continue;
            m[t].push_back(u->data);
            q.push({u->left, t - 1});
            q.push({u->right, t + 1});
        }
    }

    vector<int> verticalOrder(Node *root)
    {
        bfs(root);
        vector<int> ans;
        for (auto x : m)
        {
            for (auto v : x.second)
                ans.push_back(v);
        }
        return ans;
    }
};