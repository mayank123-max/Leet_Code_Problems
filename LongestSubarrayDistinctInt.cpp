#include<iostream>
#include<vector>
#include<unordered_set>
#include<algorithm>
using namespace std;

int Longest(vector<int> &array)
{
    int i,n = array.size(),maximum = INT_MIN;
    unordered_set<int> us;
    for(auto i:array)
    {
        if(us.find(i) == us.end())
            us.insert(i);
        else
        {
            if(us.size() > maximum)
                maximum = us.size();
            us.clear();
            us.insert(i);
        }
    }
    return maximum;
}

int main()
{
    int n;
    cin>>n;
    vector<int> array(n);
    for(int i=0;i<n;i++)
        cin>>array[i];
    cout<<Longest(array);
}