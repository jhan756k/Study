// 크루스칼 알고리즘
// 시간복잡도 --> 정렬 + Union-find

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int parent[10001];

int getParent(int x) {
	if (parent[x] == x) {
		return x;
	}
	return parent[x] = getParent(parent[x]);
}

void unionParent(int a, int b) {
	a = getParent(a);
	b = getParent(b);
	if (a < b) parent[b] = a;
	else parent[a] = b;
}

bool find(int a, int b) {
	a = getParent(a);
	b = getParent(b);
	if (a == b) return true;
	else return false;
}

int main() {
	int v, e;
	cin >> v >> e;
	int res = 0;
	vector<pair<int, pair<int, int>>> vertex;

	while (e--) { // 간선 입력
		int st, et, w;
		cin >> st >> et >> w;
		vertex.push_back({ w, {st, et} });
	}

	sort(vertex.begin(), vertex.end()); // 간선 가중치로 sort

	for (int i = 1; i <= v; i++) { // 부모 배열 초기화 (자기자신 부모 설정)
		parent[i] = i;
	}

	for (int i = 0; i < vertex.size(); i++) { // 모든 간선에 대하여

		if (!find(vertex[i].second.first, vertex[i].second.second)) {
			// 간선의 시작과 끝 노드가 같은 부모를 가지고 있지 않다면
			unionParent(vertex[i].second.first, vertex[i].second.second);
			// 부모 합쳐주고
			res += vertex[i].first; // 가중치 더하기
		}
	}
	
	cout << res;

	return 0;
}