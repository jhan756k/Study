// น้มุ 1806

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	
		

	return 0;
}

/* O(n^2) prefix sum (TLE)

#include <iostream>
#include <algorithm>
using namespace std;

int n, s, st = 0, et, tmp, res = 2147000000;
int nlist[100001];
int prefixsum[100001];

int main() {

	cin >> n >> s;
	et = n - 1;

	for (int i = 0; i < n; i++) {
		cin >> nlist[i];
	}

	prefixsum[0] = nlist[0];
	for (int i = 1; i < n; i++) {
		prefixsum[i] = prefixsum[i - 1] + nlist[i];
	}

	for (int i = 0; i < n; i++) {
		for (int j = i; j >= 0; j--) {

			if (i == j) {
				tmp = nlist[i];
			}
			else if (j == 0) {
				tmp = prefixsum[i];
			}
			else {
				tmp = prefixsum[i] - prefixsum[j - 1];
			}

			if (tmp >= s) {
				if (abs(i - j) + 1 < res) {
					res = abs(i - j) + 1;
					continue;
				}
			}
		}
	}

	if (res != 2147000000) {
		cout << res;
	}
	else {
		cout << 0;
	}

	return 0;
}

*/