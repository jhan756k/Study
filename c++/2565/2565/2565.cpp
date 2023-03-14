#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, st, et, res = 100, dpmax = 0, last;
int dp[510];
vector<pair<int, int> > v;

int main() {
	cin >> n;

	for (int i = 0; i<n; i++){
		cin >> st >> et;
		v.push_back(make_pair(st, et));
	}

	 sort(v.begin(), v.end());

	dp[0] = 1;

	for (int i = 1; i < n; i++) {
		dp[i] = 1;

		for (int k = 0; k < i; k++) {
			if (v[i].second > v[k].second) {
				if (dp[i] < dp[k] + 1) {
					dp[i] = dp[k] + 1;
				}
			}
		}
		
		dpmax = max(dpmax, dp[i]);
	}

	cout << (n-dpmax);
	return 0;
}