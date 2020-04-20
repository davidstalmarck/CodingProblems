// you can find the problem here https://open.kattis.com/problems/zamka
//  written by David Stålmarck 2020-02-26

#include <iostream>
using namespace std;

int main(){
    long int L; long int D; long int X;
    cin >> L >> D >> X;
    int localDigit = 0; int localSum; int y; long int biggest = 0;
    for (int x=L; x<=D; x++)
    {
        localSum = 0; y = x;
        while (y>0)
        {
            localDigit = y%10;
            localSum += localDigit;
            y/=10;
            //cout << localSum << endl;
        }
        if (localSum == X)
        {
            if (biggest ==0)
            {
                cout << x << endl;
            }
            biggest = x;
            
        }
    }
    cout << biggest;
}