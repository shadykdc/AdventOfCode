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
    enum { ACC, JMP, NOP } op;
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
    string op;
    while(fscanf(fp, "%s %d", &op[0], &instr.arg) == 2)
    {
        if (strcmp(&op[0], "acc") == 0)
            instr.op = Instruction::ACC;
        else if (strcmp(&op[0], "jmp") == 0)
            instr.op = Instruction::JMP;
        else if (strcmp(&op[0], "nop") == 0)
            instr.op = Instruction::NOP;
        instructions.push_back(instr);
    }
    fclose(fp);
}

bool run_game(vector<Instruction>& instructions, int* accumulator)
{
    int i = 0;
    vector<bool> run_before(instructions.size(), false);

    while (!run_before[i])
    {
        run_before[i] = true;

        switch (instructions[i].op)
        {
        case Instruction::NOP:
            i = (i + 1) % instructions.size();
            if (i == instructions.size()-1) // Part 2
                return true;
            break;
        case Instruction::ACC:
            *accumulator += instructions[i].arg;
            i = (i + 1) % instructions.size();
            if (i == instructions.size()-1) // Part 2
                return true;
            break;
        case Instruction::JMP:
            i = (i + instructions[i].arg) % instructions.size();
            break;
        default:
            cout << "Invalid operation: " << instructions[i].op << endl;
        }
    }

    return false;
}

int part2(vector<Instruction>& instructions)
{
    for (int i = 0; i < instructions.size(); i++)
    {
        int accumulator = 0;
        switch (instructions[i].op)
        {
        case Instruction::JMP:
            instructions[i].op = Instruction::NOP;
            if (run_game(instructions, &accumulator))
                return accumulator;
            instructions[i].op = Instruction::JMP;
            break;
        case Instruction::NOP:
            instructions[i].op = Instruction::JMP;
            if (run_game(instructions, &accumulator))
                return accumulator;
            instructions[i].op = Instruction::NOP;
            break;
        case Instruction::ACC:
        default:
            continue;
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
