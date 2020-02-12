#include <iostream>

using namespace std;

int main() {
	int A, B;
	while (1) {
		cin >> A;
		if (A > 0) break;
	}
	while (1) {
		cin >> B;
		if (B < 10)break;
	}
	cout << A + B;
	return 0;
}