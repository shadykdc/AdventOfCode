/*
    Advent of Code Day 11

    To run on a mac:

        1. Update makefile "DAY" variable to 11
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/11
*/

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define INPUT_FILE "input11.txt"

void read_file(vector<string>& grid)
{
    string row;
    ifstream ifs(INPUT_FILE, ifstream::in);

    while(ifs.good())
    {
        getline(ifs, row);
        grid.push_back(row);
    }
    ifs.close();
}

// count adjacent occupied seats
int count_adj_occ_seats(vector<string>& grid, size_t r, size_t c)
{
    int count = 0;

    for (int i = -1; i <= 1; i++)
    {
        for (int j = -1; j <= 1; j++)
        {
            if (i == 0 && j == 0) continue;
            if (r+i >= 0 && r+i < grid.size() &&
                c+j >= 0 && c+j < grid[c+j].size() &&
                grid[r+i][c+j] == '#')
            {
                count++;
            }
        }
    }
    return count;
}

int count_visible_occ_seats(vector<string>& grid, size_t r, size_t c)
{
    int occ_count = 0;

    // check to the down
    int i = 1;
    while (r+i < grid.size() && grid[r+i][c] == '.') i++;
    if (r+i < grid.size() && grid[r+i][c] == '#') occ_count++;

    // check to the up
    i = 1;
    while (r-i >= 0 && grid[r-i][c] == '.') i++;
    if (r-i >= 0 && grid[r-i][c] == '#') occ_count++;

    // check right
    i = 1;
    while (c+i < grid[r].size() && grid[r][c+i] == '.') i++;
    if (c+i < grid[r].size() && grid[r][c+i] == '#') occ_count++;

    // check left
    i = 1;
    while (c-i >= 0 && grid[r][c-i] == '.') i++;
    if (c-i >= 0 && grid[r][c-i] == '#') occ_count++;

    // check right down
    i = 1;
    while (r+i < grid.size() && c+i < grid[r+i].size() && grid[r+i][c+i] == '.') i++;
    if (r+i < grid.size() && c+i < grid[r+i].size() && grid[r+i][c+i] == '#') occ_count++;

    // check left down
    i = 1;
    while (r+i < grid.size() && c-i >= 0 && grid[r+i][c-i] == '.') i++;
    if (r+i < grid.size() && c-i >= 0 && grid[r+i][c-i] == '#') occ_count++;

    // check right up
    i = 1;
    while (r-i >= 0 && c+i < grid[r-i].size() && grid[r-i][c+i] == '.') i++;
    if (r-i >= 0 && c+i < grid[r-i].size() && grid[r-i][c+i] == '#') occ_count++;

    // check left up
    i = 1;
    while (r-i >= 0 && c-i >=0 && grid[r-i][c-i] == '.') i++;
    if (r-i >= 0 && c-i >=0 && grid[r-i][c-i] == '#') occ_count++;

    return occ_count;
}

// returns the number of occupied seats at the end of a shuffle
int seat_shuffle(vector<string>& grid, bool part1, int seats_limit)
{
    size_t occupied_count = 0;
    bool still_changing = true;
    vector<string> new_grid(grid.begin(), grid.end());

    while (still_changing)
    {
        still_changing = false;
        for (size_t r = 0; r < grid.size(); r++)
        {
            for (size_t c = 0; c < grid[r].size(); c++)
            {
                if (grid[r][c] == '.') continue;
                size_t adj_occ_seats = part1 ?
                                       count_adj_occ_seats(grid, r, c) :
                                       count_visible_occ_seats(grid, r, c);
                if (adj_occ_seats == 0 && grid[r][c] == 'L')
                {
                    new_grid[r][c] = '#';
                    still_changing = true;
                    occupied_count++;
                }
                else if (adj_occ_seats >= seats_limit && grid[r][c] == '#')
                {
                    new_grid[r][c] = 'L';
                    still_changing = true;
                    occupied_count--;
                }
            }
        }
        grid = new_grid;
    }

    return occupied_count;
}

int main(int argc, char *argv[])
{
    vector<string> grid;
    read_file(grid);
    cout << "Part 1: " << seat_shuffle(grid, true, 4) << endl; // 2427

    grid.clear();
    read_file(grid);
    cout << "Part 2: " << seat_shuffle(grid, false, 5) << endl; // 2199

    return 0;
}
