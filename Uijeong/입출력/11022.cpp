#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;

	int A, B;
	for (int i = 0; i < T; i++) {
		cin >> A >> B;
		cout << "Case #" << i + 1 << ": "
			<< A << " + " << B << " = " << A + B << endl;
	}
}