#include <iostream>
#include <cstring>
using namespace std;

int r, c, t, res, sc, tmpx, tmpy, spread;
int room[60][60];
int add[60][60];
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };
int upc, dpc;

void diffuse() {
	memset(add, 0, sizeof(add));

	for (int x = 1; x <= r; x++) {
		for (int y = 1; y <= c; y++) {

			if (room[x][y] != 0 && room[x][y] != -1) {
				sc = 0;
				spread = room[x][y] / 5;

				for (int d = 0; d < 4; d++) {
					tmpx = x + dx[d];
					tmpy = y + dy[d];
					if (tmpx > 0 && tmpx <= r && tmpy > 0 && tmpy <= c && room[tmpx][tmpy] != -1) {
						sc++;
						add[tmpx][tmpy] += spread;
					}
				}
				
				add[x][y] -= (spread)*sc;
			}
		}
	}

	for (int x = 1; x <= r; x++) {
		for (int y = 1; y <= c; y++) {
			room[x][y] += add[x][y];
		}
	}

	return;
}

void cleanse() {

	for (int x = upc - 1; x > 1; x--) {
		room[x][1] = room[x - 1][1];
	}

	for (int x = 1; x < c; x++) {
		room[1][x] = room[1][x + 1];
	}

	for (int x = 1; x < upc; x++) {
		room[x][c] = room[x + 1][c];
	}

	for (int x = c; x > 2; x--) {
		room[upc][x] = room[upc][x - 1];
	}

	room[upc][2] = 0;
	
	for (int x = dpc + 1; x < r; x++) {
		room[x][1] = room[x+1][1];
	}
	
	for (int x = 1; x < c; x++) {
		room[r][x] = room[r][x+1];
	}
	
	for (int x = r; x > dpc; x--) {
		room[x][c] = room[x - 1][c];
	}
	
	for (int x = c; x > 2; x--) {
		room[dpc][x] = room[dpc][x - 1];
	}

	room[dpc][2] = 0;
	

	return;
}

int main() {
	bool fir = true;
	cin >> r >> c >> t;

	for (int x = 1; x <= r; x++) {
		for (int y = 1; y <= c; y++) {
			cin >> room[x][y];
			if (room[x][y] == -1) {
				if (fir) {
					fir = false;
					upc = x;
				}
				else {
					dpc = x;
				}	
			}
		}
	}

	while (t--) {
		diffuse();
		cleanse();
	}

	for (int x = 1; x <= r; x++) {
		for (int y = 1; y <= c; y++) {
			res += room[x][y];
		}
	}
	
	cout << res+2;
	return 0;
}
