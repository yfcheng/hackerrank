/*
Reverse words : "I love to play" becomes "play to love I". 
*/
#include <iostream>
#include <string>
#include <ctype.h>
using namespace std;

string reverse_string(string input,int lowerbound,int upperbound)
{
	while(lowerbound<upperbound){
		swap(input[lowerbound],input[upperbound]);
		lowerbound++;
		upperbound--;
	}
	return input;
}

string reverse_word(string input)
{
	string reversed = reverse_string(input,0,input.length()-1);	
	int tot=0;
	int lower=0;
	while(tot <= reversed.length()){
		if(isspace(reversed[tot])){
			reversed = reverse_string(reversed,lower,tot-1);
			lower = tot+1;
		}
		tot++;
	}
	return reversed;
}

int main(){
	
	string a = "I love to play";
	cout << a << endl << reverse_word(a) << endl;
	return 0;
}
