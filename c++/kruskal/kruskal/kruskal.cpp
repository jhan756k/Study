// ũ�罺Į �˰���
// �ð����⵵ --> ���� + Union-find

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

	while (e--) { // ���� �Է�
		int st, et, w;
		cin >> st >> et >> w;
		vertex.push_back({ w, {st, et} });
	}

	sort(vertex.begin(), vertex.end()); // ���� ����ġ�� sort

	for (int i = 1; i <= v; i++) { // �θ� �迭 �ʱ�ȭ (�ڱ��ڽ� �θ� ����)
		parent[i] = i;
	}

	for (int i = 0; i < vertex.size(); i++) { // ��� ������ ���Ͽ�

		if (!find(vertex[i].second.first, vertex[i].second.second)) {
			// ������ ���۰� �� ��尡 ���� �θ� ������ ���� �ʴٸ�
			unionParent(vertex[i].second.first, vertex[i].second.second);
			// �θ� �����ְ�
			res += vertex[i].first; // ����ġ ���ϱ�
		}
	}
	
	cout << res;

	return 0;
}