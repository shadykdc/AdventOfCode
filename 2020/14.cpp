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
#include <unordered_map>
#include <bitset>
#include <string>
#include <stdio.h>
#include <vector>

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

void comb(int count_x, vector<bitset<36>>& addresses, bitset<36>& mem_addr, string mask)
{
    if (count_x == 0) addresses.emplace_back(mem_addr);

    for (int i = 0; i < mask.size(); i++)
    {
        if (mask[i] == 'X')
        {
            mask[i] = 'Y';

            mem_addr.set(mem_addr.size()-1-i, 1);
            comb(count_x-1, addresses, mem_addr, mask);

            mem_addr.set(mem_addr.size()-1-i, 0);
            comb(count_x-1, addresses, mem_addr, mask);

            break;
        }
    }
}

void populate_mem(const string str, const int idx, const string mask,
                  unordered_map<unsigned long, bitset<36>>& memory)
{
    bitset<36> val(stoi(str));
    bitset<36> mem_addr(idx);
    vector<bitset<36>> addresses;
    int count_x = 0;
    for (int i = 0; i < mask.size(); i++)
    {
        size_t mem_addr_i = mem_addr.size() - 1 - i;
        if (mask[i] == '1')  mem_addr.set(mem_addr_i, 1);
        else if (mask[i] == 'X') count_x++;
    }

    comb(count_x, addresses, mem_addr, mask);

    for (auto addr : addresses)
        memory[addr.to_ulong()] = val;
}

unsigned long part2()
{
    unordered_map<unsigned long, bitset<36>> memory;
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
            populate_mem(str, idx, mask, memory);
        }
        else if (str.size() > offset)
            mask = str.substr(offset);
    }
    ifs.close();

    unsigned long sum = 0;
    for (auto val : memory)
        sum += val.second.to_ulong();

    return sum;
}

int main(int argc, char *argv[])
{
    cout << part1() << endl; // 17481577045893
    cout << part2() << endl; //

    return 0;
}
