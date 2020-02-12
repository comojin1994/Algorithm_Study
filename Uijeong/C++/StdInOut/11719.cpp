#include<iostream>
#include<string>
using namespace std;

int main() {
	string text;
	while (!cin.eof())
	{
		getline(cin, text);
		cout << text << endl;
	}
}