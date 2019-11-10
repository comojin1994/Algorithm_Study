#include <iostream>

using namespace std;

int main() {

	int A,B;

	while (cin >> A >> B)
	{
		if (A == EOF && B == EOF) break;
		cout << A + B << endl;
	}
	
	return 0;
}