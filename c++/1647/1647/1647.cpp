#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m, res = 0, last;
int parent[100001];

int getParent(int x) {
	if (parent[x] == x) return x;
	return parent[x] = getParent(parent[x]);
}

void unionParent(int a, int b) {
	a = getParent(a);
	b = getParent(b);
	if (a < b) parent[b] = a;
	else parent[a] = b;
}

int find(int a, int b) {
	a = getParent(a);
	b = getParent(b);
	if (a == b) return true;
	else return false;
}

int main() {
	cin >> n >> m;
	vector<pair<int, pair<int, int> > > vertex;

	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		vertex.push_back({ c, {a, b} });
	}

	sort(vertex.begin(), vertex.end());

	for (int i = 1; i <= n; i++) {
		parent[i] = i;
	}

	for (int i = 0; i < vertex.size(); i++) {

		if (!find(vertex[i].second.first, vertex[i].second.second)) {
			unionParent(vertex[i].second.first, vertex[i].second.second);
			res += vertex[i].first; 
			last = vertex[i].first;
		}
	}

	cout << res-last;

	return 0;
}