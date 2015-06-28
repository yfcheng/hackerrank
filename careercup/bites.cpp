#include <bitset>
#include <iostream>
#include <stdio.h> 
#include <math.h>

using namespace std;

int to_binary(int x){
    int rem;
    int converted = 0;
    int multiplicator = 1;
    while (x > 0){
        rem = x % 2;
        x /= 2;
        converted += rem * multiplicator;
        multiplicator *= 10;
    }
    return converted;
}



int main()
{	
	cout << to_binary(1) << endl;	
	string binary = "0";
	while(binary.length() <= 3-1){
		binary += "0";		
	}
	cout << binary << endl;
	return 0;
}