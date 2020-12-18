/*
    Advent of Code Day 18

    To run on a mac:

        1. Update makefile "DAY" variable to 18
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/18
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

#define INPUT_FILE "input18.txt"

void read_file(vector<string>& equations)
{
    ifstream ifs(INPUT_FILE, ifstream::in);
    string equation;

    while (ifs.good())
    {
        getline(ifs, equation);
        std::stringstream ss(equation);
        string str;
        char ch;
        while (ss >> ch)
        {
            str.push_back(ch);
        }
        equations.push_back(str);
    }
    ifs.close();
    return;
}

int compute(string equation)
{
    stack<char> syms;
    int current = 0;
    int num;

    for (auto ch : equation)
    {
        switch(ch)
        {
        case '+':
        case '*':
            syms.push(ch);
            break;
        default: // num
            num = ch - '0';
            if (syms.size() != 0)
            {
                switch (syms.top())
                {
                case '*':
                    current *= num;
                    break;
                case '+':
                    current += num;
                    break;
                }
                syms.pop();
                syms.pop();
            }
            else
                current = ch - '0';
            syms.push('0');
        }
    }
    return current;
}

int part1(vector<string>& equations)
{
    int count = 0;
    for (auto equation : equations)
    {
        count += compute(equation);
    }
    return count;
}

int main(int argc, char *argv[])
{
    vector<string> equations;
    read_file(equations);
    cout << "Part 1: " << part1(equations) << endl;

    return 0;
}
