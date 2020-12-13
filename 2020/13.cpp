/*
    Advent of Code Day 13

    To run on a mac:

        1. Update makefile "DAY" variable to 13
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/13
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

#define INPUT_FILE "input13.txt"

int read_file(vector<pair<int,int>>& bus_ids)
{
    string str;
    int times;
    ifstream ifs(INPUT_FILE, ifstream::in);

    // read in the map of trees to grid
    if (ifs.good())
    {
        getline(ifs, str);
        times = stoi(str);
    }
    while(ifs.good())
    {
        getline(ifs, str);
        std::stringstream ss(str);
        int idx = 0;
        for (int i; ss >> i;)
        {
            bus_ids.push_back(make_pair(i, idx));
            idx++;
            while (ss.peek() == ',' || ss.peek() == 'x')
            {
                if (ss.peek() == 'x')
                {
                    idx++;
                }
                ss.ignore();
            }
        }
    }
    ifs.close();
    return times;
}

int part1(vector<pair<int,int>>& bus_ids, int time)
{
    int wait = INT_MAX;
    int best_bus = 0;

    for (auto pair : bus_ids)
    {
        int bus_id = pair.first;
        if (bus_id == -1) continue;
        for (int i = 0; i < bus_id; i++)
        {
            int depart = time + i;
            if (depart%bus_id == 0 && i < wait)
            {
                wait = i;
                best_bus = bus_id;
            }
        }
    }

    return wait * best_bus;
}

long long part2(vector<pair<int,int>>& bus_ids)
{
    bool success = false;
    long long time = 100000046082771;
    while (time%bus_ids[0].first != 0) time++;
    while (!success)
    {
        success = true;
        for (auto pair : bus_ids)
        {
            if ((time+pair.second) % pair.first != 0)
            {
                success = false;
                break;
            }
        }
        if (success) return time;
        time += bus_ids[0].first;
    }

    return time;
}

int main(int argc, char *argv[])
{
    vector<pair<int,int>> bus_ids;
    int time = read_file(bus_ids);

    cout << part1(bus_ids, time) << endl; // 3606
    cout << part2(bus_ids) << endl;

    return 0;
}
