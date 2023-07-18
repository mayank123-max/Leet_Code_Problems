#include<iostream>
using namespace std;
int main()
{
    int a,b,c,ans = 0,binA,binB,binC;
    cin>>a>>b>>c;
    for(int i=0;i<31;i++)
    {
        binC = c&(1<<i);
        binA = a&(1<<i);
        binB = b&(1<<i);
        if(binC)
        {
            if(binA == 0)
                ans++;   
            if(binB == 0)
                ans++;
        }
        else
        {
            if(binA && binB)
                ans++;
        }     
    }
    cout<<ans;
}