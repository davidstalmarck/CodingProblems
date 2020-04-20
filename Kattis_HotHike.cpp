// you can find the problem here https://open.kattis.com/problems/hothike
//  written by David Stålmarck 2020-02-26

#include <iostream>

using namespace std;
int main()
{
    int days;
    cin >> days;
    int temperatures[days];

    for (int x=0; x<days; x++)
    {
        cin >> temperatures[x];
    }

    int bestday = 0; int maxTemp=100;
    for (int y=0; y<days-2; y++)
    {
        if (temperatures[y]<maxTemp && temperatures[y+2]<maxTemp)
        {
            bestday = y;
            if (temperatures[y]>temperatures[y+2])
            {
                maxTemp = temperatures[y];
            }
            else
            {
                maxTemp = temperatures[y+2];
            }
        }
    }
    cout << bestday+1 << " " << maxTemp;
}