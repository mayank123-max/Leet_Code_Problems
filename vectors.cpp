#include<iostream>
#include<vector>
using namespace std;

void solve(vector<int> &v1)
{
    v1.push_back(5);
}
int main()
{
    int n,i;
    cin>>n;
    vector<int> v(n);
    for(i=0;i<n;i++)
    {
        cin>>v[i];
    }
    solve(v);
    cout<<"[";
    for(auto ele:v)
        cout<<ele<<",";
    cout<<"]";
}