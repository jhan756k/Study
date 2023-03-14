#include <iostream>
#include <algorithm>
using namespace std;

int n;
int nlist[100001];
int st = 0, et, res = 2147000000, tmp;
int p[2];

int main() {

	cin >> n;
	et = n - 1;
	for (int i = 0; i < n; i++) {
		cin >> nlist[i];
	}
	sort(nlist, nlist + n);

	while (st < et) {
		tmp = nlist[st] + nlist[et];

		if (abs(tmp) < abs(res)) {
			p[0] = nlist[st];
			p[1] = nlist[et];
			res = tmp;
		}

		if (tmp < 0) {
			st++;
		}
		else if (tmp > 0) {
			et--;
			
		} 
		else {
			cout << nlist[st] << " " << nlist[et];
			return 0;
		}
	}

	cout << p[0] << " " << p[1];
	return 0;
}