#include<iostream>
#include<vector>
using namespace std;
vector<int> Kadenes(vector<int> array)
{
    vector<int> kadenes;
    int i;
    kadenes.push_back(array[0]);
    for(i=1;i<array.size();i++)
    {
        if(kadenes[i-1] < 0)
            kadenes[i] = array[i];
        else
            kadenes[i] = kadenes[i-1] + array[i];
    }
    return kadenes;
}

int main()
{
    vector<int> array;
    vector<int> kadenes;
    int i,x,n;
    cout<<"Enter the no. of Elements u want in an array...\n";
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>x;
        array.push_back(x);
    }
    kadenes = Kadenes(array);
    for(i=0;i<kadenes.size();i++)
        cout<<kadenes[i]<<" ";
}