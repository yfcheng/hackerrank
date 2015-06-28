#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
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

string appendedbinary(int x,int reqLen){	
	char buffer[33];
	itoa(to_binary(x),buffer,10);
	string binary = string(buffer);	
	int i = binary.length();
	while(i < reqLen){
		binary = "0" + binary;
		i++;
	}
	return binary;
}

vector<string> get_replacements(string term){
	vector<string> patterns;
	vector<int> positions;
	for(int i=0;i<term.length();i++){
		if(term[i] == '*') {
			positions.push_back(i);
		}		
	}
	int num = positions.size();	
	if(num == 0) {			//there are no positions with *
		vector<string> new_patt;
		new_patt.push_back(term);
		return new_patt;
	}

	int i = 0;	
	string p;
	int lim = (int)pow(2,num);	
	while(i < lim){
		string binary = appendedbinary(i,num);
		p = term;
		for(int j=0;j<num;j++){			
			p[positions[j]] = binary[j];
		}		
		patterns.push_back(p);
		i++;
	}
	return patterns;
}

void print_patterns(string term){	
	vector<string> patterns = get_replacements(term);
	cout << "term = " << term << endl << "Below are patterns:" << endl;
	for(int i=0;i<patterns.size();i++){
		cout << patterns[i] << endl;
	}
	cout << "========" << endl;
}


int main(){
	print_patterns("");
	print_patterns("aa*bbb*c");
	print_patterns("aa*bbbc");
}