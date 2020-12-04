/*
    Advent of Code Day 3

    To run on a mac:

        1. Update makefile "DAY" variable to 3
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/3
*/

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define INPUT_FILE "input3.txt"

int part1(vector<string>& grid, int right, int down)
{
    int r = 0, c = 0;
    int height = grid.size();
    int width = height ? grid[0].size() : 0;
    int trees_hit = 0;

    while(r < (height - down))
    {
        c = (c + right) % width;
        r += down;

        // checking in case the input file is messed up or picks up an empty
        // line at the end or something
        if (c >= grid[r].size())
            break;

        if (grid[r][c] == '#')
            trees_hit++;
    }

    return trees_hit;
}

long long part2(vector<string>& grid)
{
    // slope pairs
    vector<int> rights = {1, 3, 5, 7, 1};
    vector<int> downs  = {1, 1, 1, 1, 2};
    long long product  = 1;

    for (int i = 0; i < rights.size() && i < downs.size(); i++)
    {
        product *= part1(grid, rights[i], downs[i]);
    }
    return product;
}

int main(int argc, char *argv[])
{
    vector<string> grid;
    string row;
    ifstream ifs(INPUT_FILE, ifstream::in);

    // read in the map of trees to grid
    while(ifs.good())
    {
        getline(ifs, row);
        grid.push_back(row);
    }
    ifs.close();

    cout << "Part 1: " << part1(grid, 3, 1) << endl;
    cout << "Part 2: " << part2(grid) << endl;

    return 0;
}
