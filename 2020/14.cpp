/*
    Advent of Code Day 14

    To run on a mac:

        1. Update makefile "DAY" variable to 14
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/14
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>
#include <string>
#include <stdio.h>

using namespace std;

#define INPUT_FILE "input14.txt"

unsigned long part1()
{
    vector<bitset<36>> memory;
    int idx;
    string str;
    string mask;
    ifstream ifs(INPUT_FILE, ifstream::in);
    int offset = strlen("mask = ");

    if (ifs.good()) getline(ifs, mask);
    if (mask.size() > offset) mask = mask.substr(7);

    while (ifs.good())
    {
        getline(ifs, str);
        if(sscanf(&str[0], "mem[%d] = %s ", &idx, &str[0]) == 2)
        {
            bitset<36> val (stoi(str));
            if (idx >= memory.size()) memory.resize(idx+1);
            for (int i = 0; i < mask.size(); i++)
            {
                if (mask[i] != 'X')
                    // the index of the bitset is "backwards"
                    val.set(val.size() - 1 - i, mask[i] - '0');
            }
            memory[idx] = val;
        }
        else if (str.size() > offset)
            mask = str.substr(offset);
    }
    ifs.close();

    unsigned long sum = 0;
    for (auto val : memory)
        sum += val.to_ulong();

    return sum;
}

unsigned long part2()
{
    vector<bitset<36>> memory;
    int idx;
    string str;
    string mask;
    ifstream ifs(INPUT_FILE, ifstream::in);
    int offset = strlen("mask = ");

    if (ifs.good()) getline(ifs, mask);
    if (mask.size() > offset) mask = mask.substr(7);

    while (ifs.good())
    {
        getline(ifs, str);
        if(sscanf(&str[0], "mem[%d] = %s ", &idx, &str[0]) == 2)
        {
            bitset<36> val (stoi(str));
            if (idx >= memory.size()) memory.resize(idx+1);
            for (int i = 0; i < mask.size(); i++)
            {
                // do something different
            }
            memory[idx] = val;
        }
        else if (str.size() > offset)
            mask = str.substr(offset);
    }
    ifs.close();

    unsigned long sum = 0;
    for (auto val : memory)
        sum += val.to_ulong();

    return sum;
}

int main(int argc, char *argv[])
{
    cout << part1() << endl; // 17481577045893
    cout << part1() << endl; //

    return 0;
}
