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
#include <unordered_set>
#include <math.h>
#include <queue>

using namespace std;

#define INPUT_FILE "input20.txt"

class Tile
{
public:
    int id;
    vector<string> pattern;
    vector<bool> compatible_edges;
    Tile(int _id = -1) { id = _id; compatible_edges = {false, false, false, false}; }

    // print tile
    void print()
    {
        cout << "Tile " << id << endl;
        for (auto str : pattern)
            cout << str << endl;
        cout << endl;
    }

    // flip horizontally
    void flip_horiz()
    {
        size_t size = pattern.size();
        for (int r = 0; r < pattern.size(); r++)
        {
            for (int i = 0; i < size/2; i++)
            {
                int temp = pattern[r][i];
                pattern[r][i] = pattern[r][size-1-i];
                pattern[r][size-1-i] = temp;
            }
        }
    }

    // flip veritcally
    void flip_vert()
    {
        size_t size = pattern.size();
        for (int i = 0; i < size/2; i++)
        {
            for (int c = 0; c < size; c++)
            {
                int temp = pattern[i][c];
                pattern[i][c] = pattern[size-1-i][c];
                pattern[size-1-i][c] = temp;
            }
        }
    }

    // rotate counter clock wise 90 degrees
    void rotateCCW()
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

    // rotate clock wise 90 degrees
    void rotateCW()
    {
        // Tiles seem to be 10 x 10 so assuming row count == col count
        int d = pattern.size()-1; // dimension
        for (int r = 0; r < pattern.size()/2; r++)
        {
            for (int c = r; c < d-r; c++)
            {
                int temp = pattern[r][c];
                pattern[r][c] = pattern[d-c][r];
                pattern[d-c][r] = pattern[d-r][d-c];
                pattern[d-r][d-c] = pattern[c][d-r];
                pattern[c][d-r]= temp;
            }
        }
    }

    // returns true if edge matches edge of Tile t
    // edge = 0 --> tile t is to the right and matches
    // edge = 1 --> tile t is below and matches
    bool matches(Tile* t, int edge)
    {
        // yay for perfect square tiles
        int dim = pattern.size();
        if (edge == 0)
        {
            for (int i = 0; i < dim; i++)
            {
                if (pattern[i][dim-1] != t->pattern[i][0])
                    return false;
            }
        }
        else if (edge == 1)
        {
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

long long part1(unordered_map<int, Tile>& tiles, vector<int>& ids)
{
    // for each tile, count how many of its edges match with other tiles
    for (int i = 0; i < ids.size(); i++) // for each tile
    {
        for (int x1 = 0; x1 < 2; x1++)
        {
            for (int edge = 0; edge < 4; edge++) // for each edge
            {
                if (tiles[ids[i]].compatible_edges[edge]) continue;
                for (int j = 0; j < ids.size(); j++) // pair with another tile
                {
                    if (i == j) continue;
                    for (int x = 0; x < 2; x++)
                    {
                        for (int edge2 = 0; edge2 < 4; edge2++)
                        {
                            if (tiles[ids[i]].matches(&tiles[ids[j]], 0))
                            {
                                tiles[ids[i]].compatible_edges[edge] = true;
                                tiles[ids[j]].compatible_edges[edge2] = true;
                            }
                            tiles[ids[j]].rotateCW();
                        }
                        tiles[ids[j]].rotateCW();
                        tiles[ids[j]].rotateCW();
                        tiles[ids[j]].flip_horiz();
                    }
                }
                tiles[ids[i]].rotateCW();
            }
            tiles[ids[i]].rotateCW();
            tiles[ids[i]].rotateCW();
            tiles[ids[i]].flip_horiz();
        }
    }
    return 1;
}

int main(int argc, char *argv[])
{
    unordered_map<int, Tile> tiles;
    vector<int> ids;
    read_file(tiles, ids);

    cout << endl << "Part 1: " << part1(tiles, ids) << endl;
    for (auto item : tiles)
    {
        int count = 0;
        for (auto edge : item.second.compatible_edges)
            if (edge) count++;
        cout << item.second.id << " " << count << endl;
    }

    return 0;
}
