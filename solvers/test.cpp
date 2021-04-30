#include<bits/stdc++.h>
using namespace std;

 void solve( vector<vector<int>> &A)   {
    int n=A.size();
    int lim1, lim2;
    if (n%2)    {
        lim1 = n/2 + 1;
        lim2 = n/2;
    }
    else    {
        lim1 = n/2;
        lim2 = n/2;
    }

    for(int i=0; i<lim1; ++i)
        for (int j=0; j<lim2; ++j)   {
            int a=A[i][j], b=A[j][n-i-1], c=A[n-i-1][n-1-j], d=A[n-1-j][i];
            A[i][j] = d;
            A[j][n-i-1] = a;
            A[n-i-1][n-1-j] = b;
            A[n-1-j][i] = c;
        }
}

int main()  {           //
    // vector<vector<int>> ar = {{1,2,3,4},
    //                           {5,6,7,8},
    //                           {9,10,11,12},
    //                           {13,14,15,16}};
    vector<vector<int>> ar = {{1,2,3},
                              {4,5,6},
                              {7,8,9}};
    solve(ar);
    for (auto a:ar)    {
        for (auto e:a)
            cout << e << " ";
        cout << endl;
    }
    return 0;
}
