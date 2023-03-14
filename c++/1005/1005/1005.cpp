#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>
#define MAX 1001
using namespace std;

int t, n, k, win;
int nlist[MAX];
int dp[MAX];

int main() {
	cin >> t;

	while (t--) {
		cin >> n >> k;

		vector<int> seq[MAX];
		int inDegree[MAX] = {0, };

		for (int i = 1; i <= n; i++) {
			cin >> nlist[i];
		}

		for (int i = 1; i <= k; i++) {
			int st, et;
			cin >> st >> et;
			seq[st].push_back(et);
			inDegree[et]++;
		}

		cin >> win;

		queue<int> q;

		for (int i = 1; i <= n; i++) {
			if (inDegree[i] == 0) {
				q.push(i);
			}
			dp[i] = nlist[i];
		}

		while (!q.empty()) {
			int now = q.front();
			q.pop();
			for (int i = 0; i < seq[now].size(); i++) {
				int tmp = seq[now][i];
				dp[tmp] = max(dp[tmp], dp[now] + nlist[tmp]);

				if (--inDegree[tmp] == 0) {
					q.push(tmp);
				}
			}
		}

		cout << dp[win] << "\n";
	}

	return 0;
}