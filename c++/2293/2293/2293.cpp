#include <iostream>
#include <algorithm>
using namespace std;

int n, k;
int coin[101];
int dp[101];

int main() {
	cin >> n >> k;

	for (int x = 0; x < n; x++) {
		cin >> coin[x];
	}
	
	for (int x = 0; x < n+10; x++) {
		dp[x] = 100;
	}

	for (int x = 0; x < n; x++) {
		for (int y = coin[x]; y < n; y++) {
			int tmp = dp[y - coin[x]] + 1;
			if (tmp < dp[x]) {
				dp[x] = tmp;
			}
		}
	}

	cout << dp[x];

	return 0;
}