#include<iostream>
#include<chrono>
#include<fstream>

using namespace std;
#define vvi vector<vector<int>>


int rlast, clast;
long iters=0;
bool solved=false;
int sdku[9][9];

bool is_available(int r, int c, int val) {
    for (int x=0; x<9; ++x) {
        if (sdku[x][c]==val)
            return false;
        if (sdku[r][x]==val)
            return false;
    }
    int gr=r-r%3, gc=c-c%3;
    for (int i=gr; i<gr+3; ++i)
        for (int j=gc; j<gc+3; ++j)
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
        for (int i=0; i<9; ++i) {
            sum1 += sdku[i][j];
            sum2 += sdku[j][i];
        }
        if (sum1!=45 || sum2!=45)
            return false;
    }
    // 3x3 grid check left
    return true;
}
void pretty_print() {   // for priting nicely
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
    cout << "\n\n";
}

bool solve()    {
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
    return check_sdku();
}


int main()  {
    ifstream puzzles("puzzles.txt");
    string row;
    int solve_count=0, nump=50;     // nump is 50 at max
    auto t1 = chrono::high_resolution_clock::now();
    
    for (int p=0; p<nump; ++p)    {
        auto t3 = chrono::high_resolution_clock::now();
        // loop start
        solved = false;

        // reading
        for (int i=-1; i<9; ++i)    {
            getline(puzzles, row);
            if (row[0]=='G')
                continue;
            for (int j=0; j<9; ++j)
                sdku[i][j] = row[j]-'0';
        }

        // solving
        bool is_solved = solve();
        auto t4 = chrono::high_resolution_clock::now();
        auto tt = chrono::duration_cast<chrono::microseconds>(t4-t3);
        if (is_solved)    {
            ++solve_count;
            printf("Solved! (%d / %d)\tTime taken: %d microseconds\n", solve_count, nump, tt.count());
        }
        else    {
            cout << "Not solved :(\n";
        }

        // displaying
        // pretty_print();

        // loop end
    }
    auto t2 = chrono::high_resolution_clock::now();
    auto t = chrono::duration_cast<chrono::microseconds>(t2-t1);
    printf("\nSolved %i/%i puzzles in %d microseconds", solve_count, nump, t.count());
    cout << " and " << iters << " total iterations.\n";
    getchar();
}
