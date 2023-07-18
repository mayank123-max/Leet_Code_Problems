#include<iostream>
#include<unordered_map>
using namespace std;

unordered_map<pair<int,int>, int> Memo;
int solve(int r, int c, int m, int n)
{
    if(r == m || c == n)
        return 0;
    if(r == m-1 && c == n-1)
        return 1;
    if(Memo.find({r,c}) != Memo.end())
        return Memo[{r,c}];
    Memo.insert({{r,c}, solve(r+1,c,m,n) + solve(r,c+1,m,n)});
    return Memo[{r,c}];
}
int main()
{
    int m,n;
    cin>>m>>n;
    cout<<solve(0,0,m,n);
}