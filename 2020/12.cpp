/*
    Advent of Code Day 12

    To run on a mac:

        1. Update makefile "DAY" variable to 12
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/12
*/

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define INPUT_FILE "input12.txt"

enum Direction { N, E, S, W };

void read_file(vector<pair<char, int>>& map)
{
    char c;
    int d;
    FILE* pfile = fopen(INPUT_FILE, "r");
    if (pfile == NULL)
    {
        cerr << "Invalid file" << endl;
        exit(1);
    }
    while(fscanf(pfile, "%c%d ", &c, &d) == 2)
    {
        map.push_back(make_pair(c, d));
    }
    fclose(pfile);
    return;
}

int part1(const vector<pair<char, int>>& map)
{
    vector<int> ship = {0, 0}; // E(+)/W(-), N(+)/S(-) absolute
    Direction dir = E; // N E S W
    int i;

    for (auto pair : map)
    {
        switch(pair.first)
        {
        case 'L': // rotate ship ccw x degrees
            for (i = 0; i < pair.second/90; i++)
            {
                switch(dir)
                {
                    case N: dir = W; break;
                    case E: dir = N; break;
                    case S: dir = E; break;
                    case W: dir = S; break;
                }
            }
            break;
        case 'R': // rotate ship cw x degrees
            for (i = 0; i < pair.second/90; i++)
            {
                switch(dir)
                {
                    case N: dir = E; break;
                    case E: dir = S; break;
                    case S: dir = W; break;
                    case W: dir = N; break;
                }
            }
            break;
        case 'F': // move ship forward x number of times
            switch(dir)
            {
                case N: ship[1] += pair.second; break;
                case E: ship[0] += pair.second; break;
                case S: ship[1] -= pair.second; break;
                case W: ship[0] -= pair.second; break;
            }
            break;
        case 'N': ship[1] += pair.second; break; // move ship N x moves
        case 'E': ship[0] += pair.second; break; // move ship E x moves
        case 'S': ship[1] -= pair.second; break; // move ship S x moves
        case 'W': ship[0] -= pair.second; break; // move ship W x moves
        }
    }
    return abs(ship[0]) + abs(ship[1]);
}

int part2(const vector<pair<char, int>>& map)
{
    vector<int> wp = {10, 1}; // E(+)/W(-), N(+)/S(-) relative to ship
    vector<int> ship = {0, 0}; // E(+)/W(-), N(+)/S(-) absolute
    int temp, i;

    for (auto pair : map)
    {
        switch(pair.first)
        {
        case 'L': // rotate waypoint around the ship ccw x degrees
            for (i = 0; i < pair.second/90; i++)
            {
                temp = wp[0];
                wp[0] = wp[1] * -1;
                wp[1] = temp;
            }
            break;
        case 'R': // rotate waypoint around the ship cw x degrees
            for (i = 0; i < pair.second/90; i++)
            {
                temp = wp[0];
                wp[0] = wp[1];
                wp[1] = temp * -1;
            }
            break;
        case 'F': // move forward to the waypoint x number of times
            for (i = 0; i < pair.second; i++)
            {
                ship[0] += wp[0];
                ship[1] += wp[1];
            }
            break;
        case 'N': wp[1] += pair.second; break; // move waypoint N x moves
        case 'E': wp[0] += pair.second; break; // move waypoint E x moves
        case 'S': wp[1] -= pair.second; break; // move waypoint S x moves
        case 'W': wp[0] -= pair.second; break; // move waypoint W x moves
        }
    }
    return abs(ship[0]) + abs(ship[1]);
}

int main(int argc, char *argv[])
{
    vector<pair<char, int>> map;
    read_file(map);
    cout << part1(map) << endl; // 904
    cout << part2(map) << endl; // 18747
    return 0;
}
