/*
    Advent of Code Day 15

    To run on a mac:

        1. Update makefile "DAY" variable to 15
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/15
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>

using namespace std;

size_t part1(vector<int>& input, int stop)
{

    // key: num; val: last turn it was spoken
    unordered_map<int, int> lookup;
    for (int i = 0; i < input.size(); i++)
        lookup[input[i]] = i + 1;

    // the turn that was just taken and the number that was just spoken
    int last_turn = input.size() + 1;
    int last_spoken = 0;

    while (last_turn < stop)
    {
        auto got = lookup.find(last_spoken);
        if (got != lookup.end())
        {
            int speak = last_turn - lookup[last_spoken];
            lookup[last_spoken] = last_turn;
            last_spoken = speak;
        }
        else
        {
            lookup[last_spoken] = last_turn;
            last_spoken = 0;
        }
        last_turn++;
    }
    return last_spoken;
}

int main(int argc, char *argv[])
{
    vector<int> input = {16,12,1,0,15,7,11};
    cout << "Part 1: " << part1(input, 2020) << endl; //403
    cout << "Part 2: " << part1(input, 30000000) << endl; // 6823

    return 0;
}
