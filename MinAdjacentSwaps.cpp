#include<iostream>
#include<vector>
#include<climits>
using namespace std;
int minMoves(vector<int>& nums, int k) {
        int minimum = INT_MIN;
        vector<int> pos;
        int len = nums.size();
        for(int i=0;i<len;i++)
        {
            if(nums[i] == 1)
                pos.push_back(i);
        }
        vector<int> prefix_sum(pos.size(),0);
        prefix_sum[nums[0]];
        for(int i=1;i<pos.size();i++)
            prefix_sum[i] = prefix_sum[i-1]+ pos[i];
            
        int size = pos.size();
        int window_len = size - k +1;
        for(int i=0;i<window_len;i++)
        {
            for(int j=i;j<k+i;j++)
            {
                int mid = k%2;
                if(k%2)
                {
                    int total_moves = (prefix_sum[k-1] - prefix_sum[mid]) - (prefix_sum[mid] - nums[i+mid]);
                    int actual_moves = total_moves - ((mid)*((mid)+1));
                    if(actual_moves < minimum)
                        minimum = actual_moves;
                }
                else
                {
                    int total_moves = (prefix_sum[k-1] - prefix_sum[mid]) - (prefix_sum[mid] - nums[i+mid]) - nums[i+mid];
                    int actual_moves = total_moves - mid*(mid+1) - (k-1-(mid));
                    if(actual_moves < minimum)
                        minimum = actual_moves;
                }
            }
        }
        return minimum;
    }
int main()
{
    int n;
    cin>>n;
    vector<int> array(n);
    int k;
    cin>>k;
    for(int i=0;i<n;i++)
        cin>>array[i];
    cout<<minMoves(array , k);
}