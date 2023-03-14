#include <iostream>
#include <vector>
#include <queue>
#define MAX 10
using namespace std;

int n, inDegree[MAX];
vector<int> a[MAX];

void topologySort() {
	int result[MAX];
	queue<int> q;

	for (int i = 1; i <= n; i++) {
		if (inDegree[i] == 0) {
			q.push(i);
		}
	}

	for (int i = 1; i <= n; i++) {
		
		if (q.empty()) {
			cout << "cycle exists";
			return;
		}

		int x = q.front();
		result[i] = x;

		for (int i = 0; i < a[x].size(); i++) {
			int y = a[x][i];

			if (--inDegree[y] == 0) {
				q.push(y);
			}
		}
	}

	for (int i = 1; i <= n; i++) {
		cout << result[i] << ", ";
	}
}

int main() {

	topologySort();

	return 0;
}
