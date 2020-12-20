/*
    Advent of Code Day 20

    To run on a mac:

        1. Update makefile "DAY" variable to 20
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/20
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <math.h>

using namespace std;

#define INPUT_FILE "input20.txt"

class Tile
{
public:
    int id;
    vector<string> pattern;
    Tile(int _id = -1) { id = _id; }

    // print tile
    void print()
    {
        cout << "Tile " << id << endl;
        for (auto str : pattern)
            cout << str << endl;
        cout << endl;
    }

    // flip horizontally
    void flip()
    {
        for (int r = 0; r < pattern.size(); r++)
        {
            size_t size = pattern[r].size();
            for (int i = 0; i < size/2; i++)
            {
                int temp = pattern[r][i];
                pattern[r][i] = pattern[r][size-1-i];
                pattern[r][size-1-i] = temp;
            }
        }
    }

    // rotate counter clock wise 90 degrees
    void rotate()
    {
        // Tiles seem to be 10 x 10 so assuming row count == col count
        int d = pattern.size()-1; // dimension
        for (int r = 0; r < pattern.size()/2; r++)
        {
            for (int c = r; c < d-r; c++)
            {
                int temp = pattern[r][c];
                pattern[r][c] = pattern[c][d-r];
                pattern[c][d-r] = pattern[d-r][d-c];
                pattern[d-r][d-c] = pattern[d-c][r];
                pattern[d-c][r] = temp;
            }
        }

    }

    // returns true if edge matches edge of Tile t
    // edge = 0 --> tile t is to the right and matches
    // edge = 1 --> tile t is below and matches
    bool matches(Tile* t, int edge)
    {
        int dim = pattern.size();
        if (edge == 0)
        {
            // yay for perfect square tiles
            for (int i = 0; i < dim; i++)
            {
                if (pattern[i][dim-1] != t->pattern[i][0])
                    return false;
            }
        }
        else if (edge == 1)
        {
            // yay for perfect square tiles
            for (int i = 0; i < dim; i++)
            {
                if (pattern[dim-1][i] != t->pattern[0][i])
                    return false;
            }
        }
        return true;
    }
};

void read_file(unordered_map<int, Tile>& tiles, vector<int>& ids)
{
    string row;
    ifstream ifs(INPUT_FILE, ifstream::in);
    Tile tile;
    vector<string> pattern;
    int tile_id;

    while(ifs.good())
    {
        getline(ifs, row);
        if (row[0] == 'T')
        {
            tile_id = stoi(row.substr(5, 4));
            tile.id = tile_id;
            tiles[tile_id] = tile;
        }
        else if (row.size() == 0)
        {
            ids.push_back(tile_id);
            tile.pattern.clear();
        }
        else
        {
            tiles[tile_id].pattern.push_back(row);
        }
    }
    ifs.close();
    return;
}

bool success(unordered_map<int, Tile>& tiles, vector<int>& ids)
{
    int dim = sqrt(ids.size()); // 3
    for (int i = 0; i < ids.size(); i++)
    {
        if ((i+1)%dim != 0 && i+1 < ids.size() && // room to right
           !tiles[ids[i]].matches(&tiles[ids[i+1]], 0)) // right matches
            return false;
        if (i+dim < ids.size() && // room below
           !tiles[ids[i]].matches(&tiles[ids[i+dim]], 1)) // down matches
            return false;
    }
    return true;
}

void find_solution(unordered_map<int, Tile>& tiles, vector<int> ids, int idx)
{
    if (success(tiles, ids)) return;



    return;
}

long part1(unordered_map<int, Tile>& tiles, vector<int>& ids)
{
    find_solution(tiles, ids, 0);

    int size = ids.size();
    int sq_rt = sqrt(size);
    return ids[0] * ids[sq_rt-1] * ids[size-sq_rt] * ids[size-1];
}

int main(int argc, char *argv[])
{
    unordered_map<int, Tile> tiles;
    vector<int> ids;
    read_file(tiles, ids);

    cout << "Part 1: " << part1(tiles, ids) << endl;

    return 0;
}
