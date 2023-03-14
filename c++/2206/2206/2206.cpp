#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <cstring>
using namespace std;

int n, m, ans=2147000000;
string board[1001];
int vis[1001][1001][2];
queue<pair<pair<int, int>, int> > dQ;
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

int BFS(int x, int y) {
	memset(vis, 0, sizeof(vis));
	vis[0][0][1] = 1;
	dQ.push({ {0, 0}, 1 });

	while (!dQ.empty()) {
		int nowx = dQ.front().first.first;
		int nowy = dQ.front().first.second;
		int block = dQ.front().second;
		dQ.pop();

		if (nowx == n - 1 && nowy == m - 1) {
			ans = min(ans, vis[nowx][nowy]);
			break;
		}

		if (nowx)

		for (int i = 0; i < 4; i++) {
			int tmpx = nowx + dx[i];
			int tmpy = nowy + dy[i];
			if (tmpx >= 0 && tmpx < n && tmpy >= 0 && tmpy < m) {
				if (board[tmpx][tmpy] == '1' && block) {
					dQ.push(make_pair(tmpx, tmpy));
					vis[tmpx][tmpy] = vis[nowx][nowy] + 1;
					block = false;
				}
				if (board[tmpx][tmpy] == '0' && vis[tmpx][tmpy]==0) {
					dQ.push(make_pair(tmpx, tmpy));
					vis[tmpx][tmpy] = vis[nowx][nowy] + 1;
				}
			}
		}
	}
	cout << "\n";
	for (int x = 0; x < n; x++) {
		for (int y = 0; y < m; y++) {
			cout << vis[x][y] << " ";
		}
		cout << "\n";
	}

	return;
}

int main() {
	cin >> n >> m;

	for (int x = 0; x < n; x++) {
		cin >> board[x];
	}

	BFS(0, 0);

	cout << BFS(0, 0);
	return 0;
}