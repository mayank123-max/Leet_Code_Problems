#include<iostream>
#include<string>
#include<vector>
#include<unordered_set>
using namespace std;

int main()
{
    int n;
    cin>>n;
    vector<string> array(n);
    for(auto &i:array)
        cin>>i;
    unordered_set<char> lookup;
    int count = 0;
    for(auto i:array)
    {
        for(auto j:i)
            lookup.insert(j);
        if(lookup.size() < 2 || lookup.size() > 2)
        {
            lookup.erase(lookup.begin(), lookup.end());
            continue;
        }
        else if(lookup.find('a') != lookup.end() && lookup.find('b') != lookup.end())
        {
            int count_a = 0, count_b = 0;
            for(auto j:i)
            {
                if(j == 'a')
                    count_a++;
                else
                    count_b++;
            }
            int tc = 1;
            int k = 1;
            if(i[0] == 'a')
            {
                while(k < count_a)
                {
                    if(i[k] == 'a')
                        tc++;
                }
                if(tc != count_a)
                    continue;
            }
            if(i[0] == 'b')
            {
                tc = 1;
                k = 1;
                while(k < count_b)
                {
                    if(i[k] == 'b')
                        tc++;
                }
                if(tc != count_b)
                    continue;
            }
            count++;
            lookup.erase(lookup.begin(), lookup.end());
        }
    }
    cout<<count;
}