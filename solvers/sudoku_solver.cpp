#include <iostream>
#include<chrono>

using namespace std;

int sdku[9][9] = 
       {{ 0, 0, 0, 0, 0, 0, 9, 0, 7 },
        { 0, 0, 0, 4, 2, 0, 1, 0, 0 },
        { 0, 0, 0, 7, 0, 5, 0, 2, 6 },
        { 1, 0, 0, 9, 0, 4, 0, 0, 0 },
        { 0, 5, 0, 0, 0, 0, 0, 4, 0 },
        { 0, 0, 0, 0, 0, 7, 0, 0, 9 },
        { 9, 0, 0, 1, 0, 8, 0, 0, 0 },
        { 0, 3, 4, 0, 5, 0, 0, 0, 0 },
        { 0, 0, 7, 0, 0, 0, 0, 0, 0 }};
    


int rlast, clast, iters=0;
bool solved=false;
bool is_available(int r, int c, int val) {
    for (int x=0; x<9; ++x) {
        if (x!=r && sdku[x][c]==val)
            return false;
        if (x!=c && sdku[r][x]==val)
            return false;
    }
    int gr=r/3, gc=c/3;
    for (int i=gr*3; i<gr*3+3; ++i)
        for (int j=gc*3; j<gc*3+3; ++j)
            if (i==r || j==c)
                continue;
            else if (sdku[i][j]==val)
                return false;
    return true;
}
void solve_cell(int r, int c)   {
    if (r==9)
        return;
    ++iters;
    int r_new=(c==8)?r+1:r, c_new=(c+1)%9;
    if (sdku[r][c])
        solve_cell(r_new, c_new);
    else    {
        for (int val=9; val>0; --val)  {
            if (is_available(r, c, val))    {
                sdku[r][c] = val;
                solve_cell(r_new, c_new);
                if (solved)
                    return;
            }
        }
        if (sdku[rlast][clast])
            solved = true;
        else
            sdku[r][c] = 0;
    }
}
bool check_sdku()   {
    for (int j=0; j<9; ++j) {
        int sum1=0, sum2=0;
        for (int i=0; i<9; ++i){
            sum1 += sdku[i][j];
            sum2 += sdku[j][i];
        }
        if (sum1!=45 || sum2!=45)
            return false;

        // 3x3 grid check left
    }
    return true;
}
void pretty_print_grid() {   // for priting nicely
    for (int i=0; i<9; ++i) {
        for (int j=0; j<9; ++j) {
            cout << sdku[i][j] << " ";
            if (j%3 == 2 && j != 8)
                cout << "| ";
        }
        cout << endl;
        if (i%3 == 2 && i != 8)
                cout << "---------------------\n";
    }
}
void print_grid()   {
    for (int i=0; i<9; ++i) {
        for (int j=0; j<9; ++j)
            cout << sdku[i][j]; // << " ";
        cout << endl;
    }
}

int main()  {
    // taking input for sudoku
    for (int i=0; i<9; ++i)
        for (int j=0; j<9; ++j)
            cin >> sdku[i][j];
    
    auto t1 = chrono::high_resolution_clock::now();
    // solving 
    for (int i=8; i>=0; --i)    {
        for (int j=8; j>=0; --j)
            if (!sdku[i][j])    {
                rlast=i;
                clast=j;
                goto k;
            }
    }
    k:
    solve_cell(0, 0);
    // solved (hopefully lol)
    auto t2 = chrono::high_resolution_clock::now();
    auto t = chrono::duration_cast<chrono::microseconds>(t2-t1);
    cout << endl;
    // pretty_print_grid();
    print_grid();
    bool check = 1;//check_sdku();
    if (check)
        cout << "\nSolved in " << t.count() << " microseconds and " 
             << iters << " iterations.";
    else
        cout << "\nNot solved. The developer sucks. Iterations: " << iters;
    return 0;
}
