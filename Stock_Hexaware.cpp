#include<iostream>
#include<vector>
#include<stack>
using namespace std;
int main()
{
    int n;
    cin>>n;
    vector<int> array(n);
    for(auto &i:array)
        cin>>i;
    vector<int> answer(n,0);
    stack<int> my_stack;
    my_stack.push(array[n-1]);
    for(int i=n-2;i>=0;i--)
    {
        int topele = my_stack.top(), c = 1;
        if(topele > array[i])
            answer[i] = 1;
        else
        {
            while(!my_stack.empty() && my_stack.top() < array[i])
            {
                my_stack.pop();
                c++;
            }
                
            if(!my_stack.empty())
                answer[i] = c;
        }
        my_stack.push(array[i]);
    }
    for(auto i:answer)
        cout<<i<<" ";
}