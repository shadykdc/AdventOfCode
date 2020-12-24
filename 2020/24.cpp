/*
    Advent of Code Day 24

    To run on a mac:

        1. Update makefile "DAY" variable to 24
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/24
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_set>
#include <math.h>

using namespace std;

#define INPUT_FILE "input24.txt"

void read_file(vector<string>& tiles)
{
    string dirs;
    ifstream ifs(INPUT_FILE, ifstream::in);

    // read in the map of trees to grid
    while(ifs.good())
    {
        getline(ifs, dirs);
        if (dirs.size())
            tiles.push_back(dirs);
    }
    ifs.close();
    return;
}

struct pair_hash
{
    size_t operator () (pair<int, int> const &pair) const
    {
        size_t h1 = hash<int>()(pair.first);
        size_t h2 = hash<int>()(pair.second);

        return h1 ^ h2;
    }
};

void get_x_y(string& dirs, int* x, int* y,
            unordered_set<pair<int, int>, pair_hash>& white_tiles)
{
    for (size_t i = 0; i < dirs.size(); i++)
    {
        if (dirs[i] == 'n' || dirs[i] == 's')
        {
            if (dirs[i] == 'n')
                *y += 1;
            else if (dirs[i] == 's')
                *y -= 1;
            if (i == dirs.size()-1)
                throw("problem");
            i++;
            if (dirs[i] == 'w')
                *x -= 1;
            else if (dirs[i] == 'e')
                *x += 1;
            else
                throw("problem");
        }
        else if (dirs[i] == 'w')
            *x -= 2;
        else if (dirs[i] == 'e')
            *x += 2;
        else
            throw("problem");
        pair<int, int> coord = make_pair(*x, *y);
        white_tiles.insert(coord);
    }
}

void get_tiles(vector<string>& tiles,
    unordered_set<pair<int, int>, pair_hash>& black_tiles,
    unordered_set<pair<int, int>, pair_hash>& white_tiles)
{
    for (auto dirs : tiles)
    {
        int x = 0;
        int y = 0;
        get_x_y(dirs, &x, &y, white_tiles);

        pair<int, int> coord = make_pair(x, y);
        auto got = black_tiles.find(coord);
        if (got == black_tiles.end())
        {
            black_tiles.insert(coord);
            if (white_tiles.find(coord) != white_tiles.end())
                white_tiles.erase(coord);
        }
        else
        {
            black_tiles.erase(coord);
            white_tiles.insert(coord);
        }
    }
}

size_t part1(vector<string>& tiles)
{
    // coordinates of black tiles
    unordered_set<pair<int, int>, pair_hash> black_tiles;
    unordered_set<pair<int, int>, pair_hash> white_tiles;
    get_tiles(tiles, black_tiles, white_tiles);
    return black_tiles.size();
}

size_t count_b_neighbors(pair<int, int> coord,
    unordered_set<pair<int, int>, pair_hash>& black_tiles,
    unordered_set<pair<int, int>, pair_hash>& white_tiles)
{
    size_t count = 0;

    coord.first -= 2; // w
    if (black_tiles.find(coord) != black_tiles.end())
        count++;
    else
        white_tiles.insert(coord);
    coord.first += 1;
    coord.second += 1; // nw
    if (black_tiles.find(coord) != black_tiles.end())
        count++;
    else
        white_tiles.insert(coord);
    coord.first += 2; // ne
    if (black_tiles.find(coord) != black_tiles.end())
        count++;
    else
        white_tiles.insert(coord);
    coord.first += 1;
    coord.second -= 1; // e
    if (black_tiles.find(coord) != black_tiles.end())
        count++;
    else
        white_tiles.insert(coord);
    coord.first -= 1;
    coord.second -= 1; // se
    if (black_tiles.find(coord) != black_tiles.end())
        count++;
    else
        white_tiles.insert(coord);
    coord.first -= 2; // sw
    if (black_tiles.find(coord) != black_tiles.end())
        count++;
    else
        white_tiles.insert(coord);
    return count;
}

void flip_tiles(
    unordered_set<pair<int, int>, pair_hash>& black_tiles,
    unordered_set<pair<int, int>, pair_hash>& white_tiles)
{
    unordered_set<pair<int, int>, pair_hash> next_black_tiles;
    unordered_set<pair<int, int>, pair_hash> next_white_tiles;

    for (auto b_coord : black_tiles)
    {
        size_t neighbors = count_b_neighbors(b_coord, black_tiles, white_tiles);
        if (neighbors == 0 || neighbors > 2)
            next_white_tiles.insert(b_coord);
        else
            next_black_tiles.insert(b_coord);
    }
    for (auto w_coord : white_tiles)
    {
        size_t neighbors = count_b_neighbors(w_coord, black_tiles, white_tiles);
        if (neighbors == 2)
            next_black_tiles.insert(w_coord);
        else
            next_white_tiles.insert(w_coord);
    }
    black_tiles = next_black_tiles;
    white_tiles = next_white_tiles;
}

size_t part2(vector<string>& tiles, size_t iterations)
{
    // coordinates of black tiles
    unordered_set<pair<int, int>, pair_hash> black_tiles;
    unordered_set<pair<int, int>, pair_hash> white_tiles;
    get_tiles(tiles, black_tiles, white_tiles);

    for (int i = 1; i < iterations+1; i++)
        flip_tiles(black_tiles, white_tiles);

    return black_tiles.size();
}

int main(int argc, char *argv[])
{
    vector<string> tiles;
    read_file(tiles);

    cout << "Part 1: " << part1(tiles) << endl; // 351
    cout << "Part 2: " << part2(tiles, 100) << endl; // 3869

    return 0;
}
