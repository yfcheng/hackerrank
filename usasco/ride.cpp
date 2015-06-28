/*
ID: senthil8
PROG: ride
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

map<char,int> alpha;

int update_map()
{
	string char_names("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
	for(int i=0;i<char_names.length();++i)
		alpha.insert(pair<char,int>(char_names[i],i+1));
	return 0;
}

int main() {
	int val = update_map();
    ofstream fout ("ride.out");
    ifstream fin ("ride.in");
    string group, comet;
    fin >> group >> comet;
    int gr_rs=1;
    int com_rs=1;
    for(int i=0;i<group.length();i++)
    	gr_rs *= alpha[group[i]];
    for(int j=0;j<comet.length();j++)
    	com_rs *= alpha[comet[j]];
    gr_rs %= 47;
    com_rs %= 47;
    if(gr_rs == com_rs % 47)
    	fout << "GO" << endl;
    else	
    	fout << "STAY" << endl;
    return 0;
}