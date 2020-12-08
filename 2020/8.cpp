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

struct Instruction
{
    int arg = 0;
    string op = "";
};

void read_file(vector<Instruction>& instructions)
{
    FILE* fp;
    fp = fopen(INPUT_FILE, "r");
    if (fp == NULL)
    {
        cout << "Invalid file" << endl;
        exit(1);
    }

    Instruction instr;
    while(fscanf(fp, "%s %d", &instr.op[0], &instr.arg) == 2)
    {
        instructions.push_back(instr);
    }
    fclose(fp);
}

bool run_game(vector<Instruction>& instructions, int* acc)
{
    int i = 0;
    vector<bool> run_before(instructions.size(), false);

    while (!run_before[i])
    {
        run_before[i] = true;

        if (strcmp(instructions[i].op.c_str(), "nop") == 0)
        {
            i = (i + 1) % instructions.size();
            if (i == instructions.size()-1) // Part 2
                return true;
        }
        else if (strcmp(instructions[i].op.c_str(), "acc") == 0)
        {
            *acc += instructions[i].arg;
            i = (i + 1) % instructions.size();
            if (i == instructions.size()-1) // Part 2
                return true;
        }
        else if (strcmp(instructions[i].op.c_str(), "jmp") == 0)
        {
            i = (i + instructions[i].arg) % instructions.size();
        }
        else
        {
            cout << "Invalid operation: " << instructions[i].op.c_str() << endl;
        }
    }

    return false;
}

int part2(vector<Instruction>& instructions)
{
    for (int i = 0; i < instructions.size(); i++)
    {
        if (strcmp(instructions[i].op.c_str(), "jmp") == 0)
        {
            instructions[i].op = "nop";
            int acc = 0;
            if (run_game(instructions, &acc)) return acc;
            instructions[i].op = "jmp";
        }
        else if (strcmp(instructions[i].op.c_str(), "nop") == 0)
        {
            instructions[i].op = "jmp";
            int acc = 0;
            if (run_game(instructions, &acc)) return acc;
            instructions[i].op = "nop";
        }
    }

    return -1;
}

int main(int argc, char *argv[])
{
    vector<Instruction> instructions;
    int accumulator = 0;

    read_file(instructions);

    assert(!run_game(instructions, &accumulator));
    cout << "Part 1: " << accumulator << endl; // 1859
    cout << "Part 2: " << part2(instructions) << endl; // 1235

    return 0;
}
