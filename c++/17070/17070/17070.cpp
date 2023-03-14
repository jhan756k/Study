#include <iostream>
#include <algorithm>
using namespace std;

// 방향 --> 0:가로 1:대각선 2:세로

int n, res = 0, tmpx, tmpy ;
int nlist[18][18];
int dx[3] = { 0, 1, 1 };
int dy[3] = { 1, 1, 0 };

bool move(int x, int y, int i) {

    tmpx = x + dx[i];
    tmpy = y + dy[i];

    if (0<tmpx && tmpx<=n && 0<tmpy && tmpy<=n && nlist[tmpx][tmpy] == 0) {
        
        if (i == 1) {
            if (nlist[tmpx - 1][tmpy] == 1 || nlist[tmpx][tmpy - 1] == 1) {
                return false;
            }
        }
        return true;
    }
    else {
        return false;
    }
}

void DFS(int x, int y, int dir) {

    if (x == n && y == n) {
        res++;
        return;
    }

    if (dir == 0) { 
        for (int na = 0; na < 2; na++) {
            if (move(x, y, na)) {
                DFS(tmpx, tmpy, na);
            }
        }
    }

    else if (dir == 1) {
        for (int nb = 0; nb < 3; nb++) {
            if (move(x, y, nb)) {
                DFS(tmpx, tmpy, nb);
            }
        } 
    }
    else if (dir == 2) {
        for (int nc = 1; nc < 3; nc++) {
            if (move(x, y, nc)) {
                DFS(tmpx, tmpy, nc);
            }
        }
    }
    return;
}

int main() {
    cin >> n;
    
    for (int a = 1; a <= n; a++) {
        for (int b = 1; b <= n; b++) {
            cin >> nlist[a][b];
        }
    }

    DFS(1, 2, 0);
    cout << res;
    return 0;
}
