#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
	int T = 0;
	int A, B;
	char del;
	
	cin >> T;
	for (int i = 0; i < T; i++){
		cin >> A >> del >> B;
		cout << A + B << endl;
	
	}

	return 0;
}