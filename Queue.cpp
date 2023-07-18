#include<iostream>
#include<vector>
#include<queue>
using namespace std;

priority_queue<int,vector<int>,greater<int>> solve(vector<int> &array)
{
    priority_queue<int,vector<int>,greater<int>> MinHeap;
    for(auto i:array)
        MinHeap.push(i);
    return MinHeap;
}

int main()
{
    int n;
    cin>>n;
    vector<int> v(n,1);
    priority_queue<int,vector<int>,greater<int>> MinHeap;
    for(int i=0;i<n;i++)
        cin>>v[i];
    MinHeap = solve(v);
    while(!MinHeap.empty())
    {
        cout<<MinHeap.top()<<"  ";
        MinHeap.pop();
    }
}