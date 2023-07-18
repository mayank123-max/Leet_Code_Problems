#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    if(n == 2)
        cout<<2;
    else if(n == 3)
        cout<<3;
    else if( (n & 1) == 0 )
        cout<<3;
    else
        cout<<4;
}