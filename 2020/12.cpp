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

int part1(vector<pair<char, int>>& map)
{
    vector<int> counts = {0, 0, 0, 0}; // N E S W
    vector<int> wp = {10, 1}; // E(+)/W, N(+)/S
    vector<int> ship = {0, 0};

    for (auto pair : map)
    {
        cout << pair.first << " " << pair.second << endl;
        if (pair.first == 'L')
        {
            int div = pair.second/90;
            for (int i = 0; i < div; i++)
            {
                int temp = wp[0];
                wp[0] = wp[1];
                wp[1] = temp * -1;
            }
        }
        else if (pair.first == 'R')
        {
            int div = pair.second/90;
            for (int i = 0; i < div; i++)
            {
                int temp = wp[0];
                wp[0] = wp[1];
                wp[1] = temp * -1;
            }
        }
        else if (pair.first == 'F')
        {
            for (int i = 0; i < pair.second; i++)
            {
                ship[0] += wp[0];
                ship[1] += wp[1];
            }
        }
        else if (pair.first == 'N')
        {
            wp[1] += pair.second;
        }
        else if (pair.first == 'E')
        {
            wp[0] += pair.second;
        }
        else if (pair.first == 'S')
        {
            wp[1] -= pair.second;
        }
        else if (pair.first == 'W')
        {
            wp[0] += pair.second;
        }
        cout << wp[0] << " " << wp[1] << " " << ship[0] << " " << ship[1] << endl;
    }
    return abs(ship[0]) + abs(ship[1]);
}

int main(int argc, char *argv[])
{
    vector<pair<char, int>> map;
    read_file(map);

    cout << part1(map) << endl;

    return 0;
}
