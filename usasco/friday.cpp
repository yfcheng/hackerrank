/*
PROB: friday
LANG: C++
*/
#include <iostream>
#include <fstream>

using namespace std;

int month[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

bool isLeap(int m) {
	return (m % 400 == 0) || ((m % 100 != 0 ) && (m % 4 == 0));
}

int days(int y, int m) {
	if(m == 1 && isLeap(y))
		return month[m] + 1;
	else 
		return month[m];
}


int main() {
	ifstream fin("friday.in");
	ofstream fout("friday.out");

	int N;
	fin>>N;

	int res[7] = {0};
	int count = 12;
	for(int y=1900; y<1900+N; y++) {
		for(int m=0; m<12; m++) {
			res[count % 7]++;	
			count += days(y, m);
		}
	}
	
	fout << res[5] << " " << res[6] << " " << res[0] << " " << res[1] << " " << res[2] << " " << res[3] << " " << res[4] << endl;
}