#include <iostream>
#include <algorithm>
using namespace std;

int r, c, ans;
char board[21][21];
bool visited[21][21];
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

void DFS(int x, int y, int v) {

	bool stuck = true;

	for (int i = 0; i < 4; i++) {
		int tmpx = x + dx[i];
		int tmpy = y + dy[i];

	}

	return;
}

int main() {

	cin >> r >> c;
	
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cin >> board[i][j];
		}
	}

	visited[0][0] = true;
	DFS(0, 0, 0);
	cout << ans;

	return 0;
}