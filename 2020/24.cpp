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
#define X_INCR 0.5   // cos(60*PI/180);
#define Y_INCR 0.866 // ...02540378; // sin(60*PI/180);

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
    size_t operator () (pair<float, float> const &pair) const
    {
        size_t h1 = hash<float>()(pair.first);
        size_t h2 = hash<float>()(pair.second);

        return h1 ^ h2;
    }
};

float rnd(float n)
{
    // round to nearest rths
    const float r = 100.0;
    n = ceil(n * r) / r;
    return n;
}

void get_x_y(string& dirs, float* x, float* y,
            unordered_set<pair<float, float>, pair_hash>& white_tiles)
{
    for (size_t i = 0; i < dirs.size(); i++)
    {
        if (dirs[i] == 'n' || dirs[i] == 's')
        {
            if (dirs[i] == 'n')
                *y += Y_INCR;
            else if (dirs[i] == 's')
                *y -= Y_INCR;
            if (i == dirs.size()-1)
                throw("problem");
            i++;
            if (dirs[i] == 'w')
                *x -= X_INCR;
            else if (dirs[i] == 'e')
                *x += X_INCR;
            else
                throw("problem");
        }
        else if (dirs[i] == 'w')
            *x -= 1;
        else if (dirs[i] == 'e')
            *x += 1;
        else
            throw("problem");
        pair<float, float> coord = make_pair(rnd(*x), rnd(*y));
        white_tiles.insert(coord);
    }
}

void get_tiles(vector<string>& tiles,
    unordered_set<pair<float, float>, pair_hash>& black_tiles,
    unordered_set<pair<float, float>, pair_hash>& white_tiles)
{
    for (auto dirs : tiles)
    {
        float x = 0;
        float y = 0;
        get_x_y(dirs, &x, &y, white_tiles);

        pair<float, float> coord = make_pair(rnd(x), rnd(y));
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
    unordered_set<pair<float, float>, pair_hash> black_tiles;
    unordered_set<pair<float, float>, pair_hash> white_tiles;
    get_tiles(tiles, black_tiles, white_tiles);
    cout << "white: " << white_tiles.size() << endl;
    return black_tiles.size();
}

size_t count_b_neighbors(pair<float, float> coord,
    unordered_set<pair<float, float>, pair_hash>& black_tiles)
{
    size_t count = 0;
    coord.first = rnd(coord.first - 1); // w
    if (black_tiles.find(coord) != black_tiles.end()) count++;
    coord.first = rnd(coord.first + X_INCR);
    coord.second = rnd(coord.second + Y_INCR); // nw
    if (black_tiles.find(coord) != black_tiles.end()) count++;
    coord.first = rnd(coord.first + 1); // ne
    if (black_tiles.find(coord) != black_tiles.end()) count++;
    coord.first = rnd(coord.first + X_INCR);
    coord.second = rnd(coord.second - Y_INCR); // e
    if (black_tiles.find(coord) != black_tiles.end()) count++;
    coord.first = rnd(coord.first - X_INCR);
    coord.second = rnd(coord.second - Y_INCR); // se
    if (black_tiles.find(coord) != black_tiles.end()) count++;
    coord.first = rnd(coord.first - 1); // sw
    if (black_tiles.find(coord) != black_tiles.end()) count++;
    coord.first = rnd(coord.first - X_INCR);
    coord.second = rnd(coord.second + Y_INCR);
    return count;
}

void flip_tiles(
    unordered_set<pair<float, float>, pair_hash>& black_tiles,
    unordered_set<pair<float, float>, pair_hash>& white_tiles)
{
    unordered_set<pair<float, float>, pair_hash> next_black_tiles;
    unordered_set<pair<float, float>, pair_hash> next_white_tiles;

    for (auto b_coord : black_tiles)
    {
        size_t neighbors = count_b_neighbors(b_coord, black_tiles);
        if (neighbors == 0 || neighbors > 2)
            next_white_tiles.insert(b_coord);
        else
            next_black_tiles.insert(b_coord);
    }
    for (auto w_coord : white_tiles)
    {
        size_t neighbors = count_b_neighbors(w_coord, black_tiles);
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
    unordered_set<pair<float, float>, pair_hash> black_tiles;
    unordered_set<pair<float, float>, pair_hash> white_tiles;
    get_tiles(tiles, black_tiles, white_tiles);

    cout << endl << "Day " << 0 << ": " << black_tiles.size() << " " << white_tiles.size() << endl;

    for (int i = 1; i < iterations+1; i++)
    {
        flip_tiles(black_tiles, white_tiles);
        if (i < 10 || i % 10 == 0)
            cout << "Day " << i << ": " << black_tiles.size() << " " << white_tiles.size() << endl;
    }

    return black_tiles.size();
}

int main(int argc, char *argv[])
{
    vector<string> tiles;
    read_file(tiles);

    cout << "Part 1: " << part1(tiles) << endl; // 351
    cout << "Part 2: " << part2(tiles, 100) << endl;

    return 0;
}
