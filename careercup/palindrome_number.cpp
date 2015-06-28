#include <iostream>


using namespace std;

bool is_palindrome(int num){
	int input_num = num;
	int digit,reversed;	
	digit = 0;
	while(num > 10){
		digit = (digit * 10) + (num%10);		
		num /= 10;
	}
	reversed = (digit*10) + num;
	return (reversed == input_num);
}


bool traverse_left_right(int num){
	if(num < 10 && num >= 0) return true;
	int left = 1;	
	int input = num;
	while(input > 10){
		left *= 10;
		input /= 10;
	}
	int left_digit,right_digit;
	int numleft,numright;
	numleft = num;
	numright = num;
	while(left > right){
		left_digit -= (numleft % left);
		right_digit = (numright % 10);
		if(left_digit != right_digit) return false;
		numleft -= (left_digit * left);
		numright /= 10;
		left /= 10;
	}	
	return true;
}

int main(){

	int num = 1200345;
	/*
	cout << is_palindrome(num) << endl;
	num = 1221;
	cout << is_palindrome(num) << endl;
	num = 0;
	cout << is_palindrome(num) << endl;
	num = 5;
	cout << is_palindrome(num) << endl;
	*/
	/*
	num = 1200345;
	cout << traverse_left_right(num) << endl;
	num = 1221;
	cout << traverse_left_right(num) << endl;
	num = 0;
	cout << traverse_left_right(num) << endl;
	num = 5;
	cout << traverse_left_right(num) << endl;
	*/
	num = 1551;
	cout << traverse_left_right(num) << endl;
	/*
	num = 15651;
	cout << traverse_left_right(num) << endl;
	*/
	return 0;
}