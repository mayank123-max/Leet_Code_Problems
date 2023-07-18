#include<iostream>
#include<vector>
using namespace std;

vector<vector<int>> subsets;
void generate(vector<int> &subset, int ind, vector<int> &array)
{
    if(ind == array.size())
    {
        subsets.push_back(subset);
        return;
    }
    generate(subset, ind+1, array);
    subset.push_back(array[ind]);
    generate(subset, ind+1, array);
    subset.pop_back();
}

int main()
{
    int n, i;
    cin>>n;
    vector<int> array(n);
    for(i=0;i<n;i++)
        cin>>array[i];
    vector<int> subset;
    generate(subset, 0, array);
    for(auto subset:subsets)
    {
        for(auto ele:subset)
            cout<<ele<<" ";
        cout<<endl;
    }
}


