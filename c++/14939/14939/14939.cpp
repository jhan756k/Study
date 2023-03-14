#include <iostream>
using namespace std;

bool lighton[15][15];
char tmp;
int dx[5] = { 1, 0, -1, 0, 0};
int dy[5] = { 0, 1, 0, -1, 0};
int cnt = 0, bsize = 5;

void printb() {
	cout << endl;
	for (int i = 0; i < bsize; i++) {
		for (int j = 0; j < bsize; j++) {
			cout << lighton[i][j];
		}
		cout << endl;	
	}
	return;
}

void change(int sx, int sy) {

	cnt++;

	for (int i = 0; i < 5; i++) {
		int tmpx = sx + dx[i];
		int tmpy = sy + dy[i];
		if (tmpx >= 0 && tmpx < bsize && tmpy >= 0 && tmpy < bsize) {
			lighton[tmpx][tmpy] = !lighton[tmpx][tmpy];
		}
	}

	return;
}

int main() {
	
	for (int i = 0; i < bsize; i++) {
		for (int j = 0; j < bsize; j++) {
			cin >> tmp;
			if (tmp == 'O') {
				lighton[i][j] = true;
			}
			else if (tmp == '#') {
				lighton[i][j] = false;
			}
		}
	}

	for (int i = 1; i < bsize; i++) {
		for (int j = 0; j < bsize; j++) {
			if (lighton[i - 1][j]) {
				change(i, j);
				printb();
			}
		}
	}

	for (int i = 0; i < bsize; i++) {
		if (lighton[bsize-1][i]) {
			cout << -1;
			return 0;
		}
	}
	
	cout << cnt;

	return 0;
}