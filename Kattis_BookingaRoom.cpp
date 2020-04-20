// you can find the problem here https://open.kattis.com/problems/bookingaroom
//  written by David Stålmarck 2017-09-10

#include <bits/stdc++.h>

using namespace std;

int main () {
    int r, n, c;
    cin >> r >> n;
    vector<bool> isRemoved(r);
    for (int i=0; i<n; ++i){
        int room;
        cin>>room;
        isRemoved[room-1] = true;
    }
    if(r==n){
    cout << "too late";
    } else {
        for (int i=0; i<r; ++i){
            if(isRemoved[i]==false){
                cout << i + 1<< endl;
                break;
            }
        }
    }
}