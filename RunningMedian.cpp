#include<iostream>
#include<vector>
#include<queue>
#define MAHS MaxHeap.size()
#define MIHS MinHeap.size()
using namespace std;

int RunningMedian(vector<int> &array)
{
    priority_queue<int> MaxHeap;
    priority_queue<int,vector<int>,greater<int>> MinHeap;
    int Median;
    for(int i=0;i<array.size();i++)
    {
        if(MAHS == 0)           // Initial Case When First Element Of Stream Is Processed Both Max And Min Heaps are empty...
            MaxHeap.push(array[i]);

        else if(MIHS == 0)      // When MinHeap is empty...
        {
            if(array[i] > MaxHeap.top())
                MinHeap.push(array[i]);
            else
            {
                int temp = MaxHeap.top();
                MinHeap.push(temp);
                MaxHeap.pop();
                MaxHeap.push(array[i]);
            }
        }
        else if(MAHS == MIHS)
        {
            if(array[i] < MinHeap.top())
                MaxHeap.push(array[i]);
            else if(array[i] > MinHeap.top())
            {
                int temp = MinHeap.top();
                MaxHeap.push(temp);
                MinHeap.pop();
                MinHeap.push(array[i]);
            }
        }
        else
        {
            if(array[i] > MaxHeap.top())
                MinHeap.push(array[i]);
            else if(array[i] < MaxHeap.top())
            {
                int temp = MaxHeap.top();
                MinHeap.push(temp);
                MaxHeap.pop();
                MaxHeap.push(array[i]);
            }
        }
    }
    if(MaxHeap.size() > MinHeap.size())
        return MaxHeap.top();
    else
        return (MaxHeap.top() + MinHeap.top())/2;
}
int main()
{
    int n;
    cin>>n;
    vector<int> v(n);
    for(int i=0;i<n;i++)
        cin>>v[i];
    cout<<RunningMedian(v);
}