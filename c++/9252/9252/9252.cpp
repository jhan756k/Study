#include <iostream>
#include <string>
#include <algorithm>
#include <stack>
using namespace std;

string str1, str2;

int lcs[1001][1001];

int main() {

	string tmp1, tmp2;
	cin >> tmp1 >> tmp2;
	str1 = '0' + tmp1;
	str2 = '0' + tmp2;

	int len1 = str1.size();
	int len2 = str2.size();

	for (int i = 0; i < len1; i++) {
		for (int j = 0; j < len2; j++) {
			if (i == 0 || j == 0) {
				lcs[i][j] = 0;
				continue;
			}

			if (str1[i] == str2[j]) {
				lcs[i][j] = lcs[i - 1][j - 1] + 1;
			}
			else {
				lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1]);
			}
		}
	}

	cout << lcs[len1 - 1][len2 - 1] << endl;

	int i = len1 - 1;
	int j = len2 - 1;
	stack<int> pathstring;

	while (lcs[i][j] != 0) {
		if (lcs[i][j] == lcs[i][j - 1]) {
			j--;
		}
		else if (lcs[i][j] == lcs[i - 1][j]) {
			i--;
		}

		else if (lcs[i][j] - 1 == lcs[i - 1][j - 1]) {
			pathstring.push(i);
			i--;
			j--;
		}
	}

	while (!pathstring.empty()) {
		cout << str1[pathstring.top()];
		pathstring.pop();
	}

	return 0;
}