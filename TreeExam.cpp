#include<iostream>
#include<vector>
using namespace std;
struct Node
{
    int val;
    Node *left,*right;
    Node(int data)
    {
        val = data;
        left,right = NULL;
    }
};

Node* insertBst(Node *root, int value)
{
    if(root == NULL)
        return new Node(value);
    if(value < root->val)
        root->left = insertBst(root->left, value);
    else
        root->right = insertBst(root->right, value);
    return root;
}

void inorder(Node *root, vector<int> &answer)
{
    if(root == NULL)
        return;
    inorder(root->left, answer);
    answer.push_back(root->val);
    inorder(root->right, answer);
}

int main()
{
    Node *root = NULL;
    int n,i;
    cin>>n;
    vector<int> elements(n);
    vector<int> answer(n);
    for(i=0;i<n;i++)
        cin>>elements[i];
    for(auto ele:elements)
        root = insertBst(root, ele);
    inorder(root, answer);
    for(auto ele:answer)
        cout<<ele<<" ";
}