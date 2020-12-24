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
    size_t id;
    vector<string> pattern;
    // map edge to list of tile ids it matches
    unordered_map<size_t, unordered_set<size_t>> compatible_edges;

    Tile(size_t _id = -1) { id = _id; }

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
    // edge = 2 --> tile t is to the left and matches
    // edge = 3 --> tile t is above and matches
    bool matches(Tile* t, size_t edge)
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
        else if (edge == 2)
        {
            for (int i = 0; i < dim; i++)
            {
                if (pattern[i][0] != t->pattern[i][dim-1])
                    return false;
            }
        }
        else if (edge == 3)
        {
            for (int i = 0; i < dim; i++)
            {
                if (pattern[0][i] != t->pattern[dim-1][i])
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

// for each tile, count how many of its edges match with other tiles edges
// no need to check both faces for both tiles (just makes duplicates)
void count_compatible_edges(unordered_map<int, Tile>& tiles, vector<int>& ids)
{
    for (size_t i = 0; i < ids.size(); i++) // for each tile
    {
        for (size_t edge1 = 0; edge1 < 4; edge1++) // for each edge
        {
            for (size_t j = i + 1; j < ids.size(); j++) // pair with another tile
            {
                for (size_t x2 = 0; x2 < 2; x2++) // for each other face
                {
                    for (size_t edge2 = 2; edge2 < 6; edge2++) // for each other edge
                    {
                        if (tiles[ids[i]].matches(&tiles[ids[j]], 0))
                        {
                            auto* c1 = &tiles[ids[i]].compatible_edges;
                            auto* c2 = &tiles[ids[j]].compatible_edges;
                            unordered_set<size_t> temp_set;
                            if (c1->find(edge1) == c1->end())
                                c1->insert(make_pair(edge1, temp_set));
                            (*c1)[edge1].insert(ids[j]);
                            if (c2->find(edge2%4) == c2->end())
                                c2->insert(make_pair(edge2%4, temp_set));
                            (*c2)[edge2%4].insert(ids[i]);
                        }
                        if (x2) tiles[ids[j]].rotateCW();
                        else tiles[ids[j]].rotateCCW();
                    }
                    tiles[ids[j]].flip_vert();
                }
            }
            tiles[ids[i]].rotateCCW();
        }
        tiles[ids[i]].flip_vert();
    }
}

long long part1(unordered_map<int, Tile>& tiles, vector<int>& ids)
{
    count_compatible_edges(tiles, ids);

    long long prod = 1;
    for (auto tile : tiles)
    {
        cout << tile.second.id << ": " << tile.second.compatible_edges.size() << endl;
        if (tile.second.compatible_edges.size() == 2)
            prod *= tile.second.id;
    }
    return prod;
}

void get_solution(unordered_map<int, Tile>& tiles, vector<int>& ids)
{
    return;
}

size_t part2(unordered_map<int, Tile>& tiles, vector<int>& ids)
{
    get_solution(tiles, ids);
    return 1;
}

int main(int argc, char *argv[])
{
    unordered_map<int, Tile> tiles;
    vector<int> ids;
    read_file(tiles, ids);

    cout << "Part 1: " << part1(tiles, ids) << endl; // 108603771107737
    cout << "Part 2: " << part2(tiles, ids) << endl; //

    return 0;
}
