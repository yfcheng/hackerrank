/* string ispalindrome or not */

#include <iostream>
#include <string>
#include <ctype.h>

using namespace std;

bool is_palindrome(string a)
{
	if(a.length() == 0){
		return true;
	}
	
	int left,right;
	left = 0;
	right = a.length() - 1;
	while(true){
		if(left >= right){
			return true;
		}

		if(ispunct(a[left]) || isspace(a[left])){
			left++;
			continue;
		}

		if(ispunct(a[right]) || isspace(a[right])){
			right--;
			continue;
		}

		if(tolower(a[left]) != tolower(a[right])){
			return false;
		}
		left++;
		right--;
	}
}

int main()
{
	cout << is_palindrome("racecar") << endl;
	cout << is_palindrome("mala") << endl;
	cout << is_palindrome("A Man, A Plan, A Canal-Panama!") << endl;
	return 0;
}