/*
    Advent of Code Day 8

    To run on a mac:

        1. Update makefile "DAY" variable to 8
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/8
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

#define INPUT_FILE "input8.txt"

void read_file(vector<pair<string, int>>& instructions)
{
    FILE* fp;
    fp = fopen(INPUT_FILE, "r");
    if (fp == NULL)
    {
        cout << "Invalid file" << endl;
        exit(1);
    }

    string op;
    int arg;
    while(fscanf(fp, "%s %d", &op[0], &arg) == 2)
    {
        instructions.push_back(make_pair(op, arg));
    }
    fclose(fp);
}

bool run_game(vector<pair<string, int>>& instructions, int* acc)
{
    int i = 0;
    vector<bool> run_before(instructions.size(), false);

    while (!run_before[i])
    {
        char* op = &instructions[i].first[0];
        int arg = instructions[i].second;
        run_before[i] = true;

        if (strcmp(op, "nop") == 0)
        {
            i = (i + 1) % instructions.size();
            if (i == instructions.size()-1) // Part 2
                return true;
        }
        else if (strcmp(op, "acc") == 0)
        {
            *acc += arg;
            i = (i + 1) % instructions.size();
            if (i == instructions.size()-1) // Part 2
                return true;
        }
        else if (strcmp(op, "jmp") == 0)
        {
            i = (i + arg) % instructions.size();
        }
        else
        {
            cout << "Invalid operation: " << op << endl;
        }
    }

    return false;
}

int part2(vector<pair<string, int>>& instructions)
{
    for (int i = 0; i < instructions.size(); i++)
    {
        if (strcmp(instructions[i].first.c_str(), "jmp") == 0)
        {
            instructions[i].first = "nop";
            int acc = 0;
            if (run_game(instructions, &acc)) return acc;
            instructions[i].first = "jmp";
        }
        else if (strcmp(instructions[i].first.c_str(), "nop") == 0)
        {
            instructions[i].first = "jmp";
            int acc = 0;
            if (run_game(instructions, &acc)) return acc;
            instructions[i].first = "nop";
        }
    }

    return -1;
}

int main(int argc, char *argv[])
{
    vector<pair<string, int>> instructions;
    int accumulator = 0;

    read_file(instructions);

    assert(!run_game(instructions, &accumulator));
    cout << "Part 1: " << accumulator << endl; // 1859
    cout << "Part 2: " << part2(instructions) << endl; // 1235

    return 0;
}
