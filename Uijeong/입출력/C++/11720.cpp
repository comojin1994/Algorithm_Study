#include <iostream>

using namespace std;

int main() {
	int N, tmp;
	int sum = 0;
	char num;

	cin >> N;
	cin.get();
	for (int i = 0; i < N; i++)
	{
		cin.get(num);
		tmp = num - '0';
		sum += tmp;
	}
	cout << sum << endl;
	
}