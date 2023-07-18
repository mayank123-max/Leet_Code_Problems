#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;

int main()
{
    int n, mind = -1;
    cin>>n;
    vector<int> array(n);
    vector<int> LIS(n,1);
    vector<int> LIS_Sequence;
    for(auto &i:array)
        cin>>i;
    for(int i=1;i<n;i++)
    {
        for(int j=0;j<i;j++)
        {
            if(array[i] > array[j] and LIS[i] <= LIS[j])
                LIS[i] = LIS[j] + 1;
        }
    }
    for(auto i:LIS)
        cout<<i<<" ";
    cout<<"\n";
    // cout<<*max_element(LIS.begin(), LIS.end());

    int me = *max_element(LIS.begin(), LIS.end());
    int i = 1, k=0;
    while(i <= me)
    {
        if(LIS[k] == i)
        {
            LIS_Sequence.push_back(array[k]);
            i++;
        }
        k++;
    }
    for(auto ele:LIS_Sequence)
        cout<<ele<<" ";
}