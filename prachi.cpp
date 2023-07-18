#include<iostream>
#include<vector>
using namespace std;


int minimum(vector<int> &array, int start, int end)
{

}

int main()
{
    int n, x,mini = 0, minind = -1;
    cin>>n;
    int temp = n;
    vector<int> array;
    while(temp--)
    {
        cin>>x;
        array.push_back(x);
    }
    for(int i=0;i<n;i++)
    {
        if(array[i] < mini)
        {
            mini = array[i];
            minind = i;
        }
    }
    if(minind)
}