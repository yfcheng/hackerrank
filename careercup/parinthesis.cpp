#include<iostream>
#include<string>
using namespace std;

void print_parentheses(int n);
void print(int left, int right, int n, string s);

int main()
{
        int n;
        cout<<"Enter n: ";
        cin>>n;
        print_parentheses(n);
}

void print_parentheses(int n)
{
        string s="";
        print(0, 0, n, s);
}

void print(int left, int right, int n, string s)
{
        if(left>n || right>n || right>left)
                return;
        if(left==right && left+right==2*n)
        {
                cout<<s<<endl;
                return;
        }
        print(left+1, right, n, s+"(");
        print(left, right+1, n, s+")");
}