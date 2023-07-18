#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;

void solve(vector<int> &array)
{
    map<int,int,greater<int>> freq;
    for(auto i:array)
        freq[i]++;
    cout<<"{";
    for(auto i:freq)
        cout<<i.first<<":"<<i.second<<",";
    cout<<"}";
}
int main()
{
    int n;
    cin>>n;
    vector<int> array(n);
    vector<int> answer;
    for(int i=0;i<n;i++)
        cin>>array[i];
    sort(array.begin(),array.end());
    solve(array);
    // for(auto i:answer)
    //     cout<<i<<" ";
}