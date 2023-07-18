#include<iostream>
#include<vector>
using namespace std;

int LIS(vector<int> &array, int n)
{
    vector<int> dp(n,0);
    dp[0] = 1;
    for(int i=1;i<n;i++)
    {
        if(array[i] > array[i-1])
            dp[i] = dp[i-1]+1;
        else
            dp[i] = dp[i-1];
    }
    return dp[n-1];
}

int main()
{
    int n, result;
    cin>>n;
    vector<int> array(n);
    for(int i=0;i<n;i++)
        cin>>array[i];
    result = LIS(array, n);
    cout<<result;   
}