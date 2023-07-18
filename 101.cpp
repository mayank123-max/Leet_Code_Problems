#include<iostream>
using namespace std;
int main()
{
    int k = 1;
    int total = 0;
    do
    {
        total = total + (k*k);
        k++;
    } while (total < 100);
   cout<<k; 
}