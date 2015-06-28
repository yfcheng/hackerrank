/*
"You have a string lets say "ABC" now write a program that prints out all the permutations of this string (for example: ACB, BAC, BCA...)" 
*/

#include <iostream>
#include <string>

using namespace std;

void permute(string data,string val,int runner)
{
	if(runner >= data.length){
		cout << val << endl;
	}
	for(int i=0;i<data.length;i++){
		string next = data.at(i);
		string remaining = data.substr(0,i) + data.substr(i+1);
		permute(next,remaining,runner+1);
	}
}


int main()
{
	permute("ABC","",0); 
	return 0;
}