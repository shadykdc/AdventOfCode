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

int read_file(vector<int>& bus_ids)
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
        for (int i; ss >> i;)
        {
            bus_ids.push_back(i);
            while (ss.peek() == ',' || ss.peek() == 'x')
            {
                if (ss.peek() == 'x')
                    bus_ids.push_back(-1);
                ss.ignore();
            }
        }
    }
    ifs.close();
    return times;
}

int part1(vector<int>& bus_ids, int time)
{
    int wait = INT_MAX;
    int bus_id = 0;

    for (int num : bus_ids)
    {
        if (num == -1) continue;
        for (int i = 0; i < num; i++)
        {
            int depart = time + i;
            if (depart%num == 0 && i < wait)
            {
                wait = i;
                bus_id = num;
            }
        }
    }

    return wait * bus_id;
}

int part2(vector<int>& bus_ids)
{
    return 1;
}

int main(int argc, char *argv[])
{
    vector<int> bus_ids;
    int time = read_file(bus_ids);

    cout << part1(bus_ids, time) << endl; // 3606
    cout << part2(bus_ids) << endl;

    return 0;
}
