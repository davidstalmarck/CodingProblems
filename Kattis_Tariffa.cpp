// you can find the problem here https://open.kattis.com/problems/tariffa
//  written by David Stålmarck 2017-09-09


#include <iostream>

using namespace std;

int main () {
int a, b,c=0;

cin >> a >> b;
    for (int i=0;i < b; i++){
    int p;
    cin >> p;
    c = a + c- p;
    }
    c = c + a;
    cout << c << endl;
}
