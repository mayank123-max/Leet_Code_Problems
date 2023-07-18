#include<iostream>
using namespace std;
int test = 0;
int main()
{
    int test = 0;
    ::test1 = 1;
    test = 2;
    cout<<::test << " " << test;
    return 0;
}