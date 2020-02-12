#include <iostream>
#include <string>
using namespace std;

int main() {
	string text;
	cin >> text;
	for (int i = 0; i < text.length() / 10 + 1; i++) {
		cout << text.substr(i * 10, 10) << endl;
	}

}