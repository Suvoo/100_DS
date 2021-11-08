int ret = 0;
int helper(Node *root,int x){
    if(!root)
        return 0;
    int lft = helper(root->left,x);
    int rgt = helper(root->right,x);
    if(lft + rgt + root->data == x)
        ret++;
    return lft + rgt  + root->data;
}
int countSubtreesWithSumX(Node* root, int X)
{
	ret = 0;
	helper(root,X);
	return ret;
}