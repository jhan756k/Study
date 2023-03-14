#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int n, m, nowx, nowy, ans = 0, res = 0;
int nlist[10][10];
int copylist[10][10];
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

void copyMap(int (*a)[10], int (*b)[10]) {
	for (int x = 0; x < n; x++) {
		for (int y = 0; y < m; y++) {
			a[x][y] = b[x][y];
		}
	}
}

void spread() {

	int tmplist[10][10];
	copyMap(tmplist, copylist);
	queue<pair<int, int> > dQ;

	for (int x = 0; x < n; x++) {
		for (int y = 0; y < m; y++) {
			if (copylist[x][y] == 2) {
				dQ.push(make_pair(x, y));
			}
		}
	}

	while (!dQ.empty()) {
		nowx = dQ.front().first;
		nowy = dQ.front().second;
		dQ.pop();

		for (int i = 0; i < 4; i++) {
			int tmpx = nowx + dx[i];
			int tmpy = nowy + dy[i];
			if (tmpx >= 0 && tmpx < n && tmpy >= 0 && tmpy < m) {
				if (tmplist[tmpx][tmpy] == 0) {
					dQ.push(make_pair(tmpx, tmpy));
					tmplist[tmpx][tmpy] = 2;
				}	
			}
		}
	}
	res = 0;
	for (int x = 0; x < n; x++) {
		for (int y = 0; y < m; y++) {
			if (tmplist[x][y] == 0) {
				res++;
			}
		}
	}
	ans = max(ans, res);
	return;
}

void wall(int v) {
	if (v == 3) {
		spread();
		return;
	}

	for (int x = 0; x < n; x++) {
		for (int y = 0; y < m; y++) {
			if (copylist[x][y] == 0) {
				copylist[x][y] = 1; 
				wall(v + 1);
				copylist[x][y] = 0;
			}
		}
	}
}

int main() {
	cin >> n >> m;

	for (int x = 0; x < n; x++) {
		for (int y = 0; y < m; y++) {
			cin >> nlist[x][y];
		}
	}

	for (int x = 0; x < n; x++) {
		for (int y = 0; y < m; y++) {
			if (nlist[x][y] == 0) {
				copyMap(copylist, nlist);
				copylist[x][y] = 1;
				wall(1);
				copylist[x][y] = 0;
			}
		}
	}
	cout << ans;

	return 0;
}
