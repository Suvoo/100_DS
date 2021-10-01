bool isbst(Node * root,Node * min, Node * max){
        if(root==NULL) return true;
        
        if(min!=NULL and root->data <=min->data){
            return false;
        }
        if(max!=NULL and root->data >=max->data){
            return false;
        }
        
        bool isleftvalid=isbst(root->left,min,root);
        
        bool isrightvalid=isbst(root->right,root,max);
        
        return isleftvalid and isrightvalid;
        
        
    }
    
    bool isBST(Node* root) 
    {
        // Your code here
        
         bool c=isbst(root,NULL,NULL);
         return c;
    }