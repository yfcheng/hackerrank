#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctype.h>

using namespace std;

string longestpalindrome(string p){
	if(p.length() == 0) return "";
	if(p.length() == 1) return p;
	int len = p.length();
	string longest = p.substr(0,1);	//even the single char
	for(int i=1;i<len-1;i++){
		//find all possible centers which can the middle char of a palindrome
		int l = i,r = i;
		while(l >= 0 && r <= p.length()-1){
			if(ispunct(p[l]) || isspace(p[l])){
				l--;
				continue;
			}
			if(ispunct(p[r]) || isspace(p[r])){
				r++;
				continue;
			}			

			if(tolower(p[l]) == tolower(p[r])){
				l--;
				r++;
			}
			else{
				break;
			}
		}

		string temp1 = p.substr(l+1,r-l-1);
		if(temp1.length() > longest.length()) longest = temp1;
	
		l = i; r = i + 1;
		while(l >= 0 && r <= p.length()-1){
			if(ispunct(p[l]) || isspace(p[l])){
				l--;
				continue;
			}
			if(ispunct(p[r]) || isspace(p[r])){
				r++;
				continue;
			}			

			if(tolower(p[l]) == tolower(p[r])){
				l--;
				r++;
			}
			else{
				break;
			}
		}
		temp1 = p.substr(l+1,r-l-1);
		if(temp1.length() > longest.length()) longest = temp1;		
	}
	return longest;
}


int main(){

	vector<string> patterns;
	patterns.push_back(" ");
	patterns.push_back("a");
	patterns.push_back("aba");
	patterns.push_back("abac");
	patterns.push_back("abacdgfdcabaaasyii,!!");
	patterns.push_back("asd A dog, a plan, a canal: pagoda.addd");
	patterns.push_back("A Toyota! Race fast, safe car! A Toyota!sasdfq3");
	patterns.push_back("aasdss fd Are we not pure? 'No sir!' Panama's moody Noriega brags. 'It is garbage!' Irony dooms a man; a prisoner up to new era. adfaafdasf");
	
	for(int i=0;i<patterns.size();i++){
		cout << patterns[i] << "=> " << longestpalindrome(patterns[i]) << endl;
	}	
	return 0;	
}