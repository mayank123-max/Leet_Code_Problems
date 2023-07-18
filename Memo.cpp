#include<iostream>
#include<unordered_map>
using namespace std;

int main()
{
    unordered_map<pair<int,int>, int> Memo;
    Memo.insert({{0,1}, 1});
    Memo.insert({{1,2}, 2});
    Memo.insert({{2,3}, 3});

    for(auto it:Memo)
    {
        cout<<it->first<<" "<<it->second;
    }
}