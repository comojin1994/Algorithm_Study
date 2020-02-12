#include<iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	if (N > 100000)return 0;
	for (int i = N; i >0; i++)
		printf("%d\n", i);
}