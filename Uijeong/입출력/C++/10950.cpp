#include <iostream>

using namespace std;

int main() {
	int testcase;
	cin >> testcase;

	int A[120], B[120];
	for (int i = 0; i < testcase; i++) {
		while (1) {
			cin >> A[i];
			if (A[i] > 0) break;
		}
		while (1) {
			cin >> B[i];
			if (B[i] < 10)break;
		}
	}
	for (int i = 0; i < testcase; i++)
		cout << A[i] + B[i] << endl;
	return 0;
}