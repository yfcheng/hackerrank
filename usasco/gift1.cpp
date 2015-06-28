/*
PROB: gift1
LANG: C++
*/
#define pb push_back
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std;
typedef pair<string, int> psi;

int main() {
	ifstream fin("gift1.in");
	ofstream fout("gift1.out");

	int N;
	string name;
	string giver;
	string receiver;
	int total;
	int rounds;
	map<string, int> balance;
	vector<string> names;
	

	fin >> N;
	for(int i=0; i<N; i++) {
		fin >> name;
		balance[name] = 0;
		names.pb(name);
	}

	for(int i=0; i<N; i++) {
		fin >> giver;
		fin >> total >> rounds;
		if(rounds == 0 || total == 0)	continue;
		int gift = total / rounds;
		for(int j=0; j<rounds; j++) {
			fin >> receiver;
			balance[receiver] += gift;
			balance[giver] -= gift;
		}
	}
	for(int i=0; i<names.size(); i++)	fout << names[i] << " " << balance[names[i]] << endl;	
}