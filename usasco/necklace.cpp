/*
ID: erbenmo2
PROG: beads
LANG: C++
*/
#define pb push_back
#define sz size
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;
typedef vector<int> vi;
typedef vector<char> vc;

vc beads;

int buf(int a) {
	if(a < 0) return buf(beads.sz() + a);
	else return a % beads.sz();
}

int findWhite(int right) {
	if(beads[right] != 'w')	return -1;
	while(beads[buf(right-1)] == 'w') {
		right = buf(right - 1);
	}
	return right;
}

int main() {
	ifstream fin("beads.in");
	ofstream fout ("beads.out");

	string beadsStr;
	int temp;
	fin>>temp;
	fin>>beadsStr;
	
	for(int i=0; i<beadsStr.length(); i++)	beads.pb(beadsStr.at(i));	


	int left = 0, mid = 0, right = 0, white = -1, max = 0;
	int leftCount = 0, rightCount = 0;

	for(int i=0; i<beads.size(); i++) {
		if(beads[i] == 'w') {
			int left = buf(i-1);
			int right = buf(i+1);
			while(beads[left] == 'w' && left != i)	left = buf(left-1);
			while(beads[right] == 'w' && right != i)	right = buf(right+1);

			if(beads[left] == beads[right]) {
				for(int j=left; j != right; j = buf(j+1))
					beads[j] = beads[left];
			}
		}
	}
	
	bool virgin = true;
	for(int i=0; i<beads.size(); i++) {
		if(beads[i] != beads[buf(i+1)]) {
			virgin = false;
			break;
		}
	}

	if(virgin) {
		fout << beads.size() << endl;
		return 0;
	}

	mid = beads.size() - 1;
	for(int i=1; i<beads.size(); i++) {
		if(beads[i] != beads[0] && beads[i] != 'w') {
			right = i;
			break;
		}
	}
	right--;

	while(true) {
		if(white != -1)	left = white;
		else			left = buf(mid + 1);
		

		mid = right;
		leftCount = 0;
		for(int i=left; i != mid; i=buf(i+1))	leftCount++;
		leftCount++;
		
		white = findWhite(right);
		if(white < left)	white = -1;

		right = buf(right + 1);
		rightCount = 1;

		if(left > right)	break;
		
		int rr = right;
		while(true) {
			rr = buf(rr+1);
			if(beads[rr] != beads[right]) {
				if(beads[rr] != 'w') {
					rr = buf(rr-1);
					break;
				}
			}
			rightCount++;
		}
		right = rr;
		
		if(leftCount + rightCount >= max) {
			max = leftCount + rightCount;
		}

	}
	fout << max << endl;
}