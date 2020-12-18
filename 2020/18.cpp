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
        equations.push_back(equation);
    }
    ifs.close();
    return;
}

int compute(string equation)
{
    stack<char> syms;
    char ch;
    int current = 0;
    int num;
    std::stringstream ss(equation);

    while (ss >> ch)
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
                    syms.pop();
                    current *= num;
                    syms.pop();
                    break;
                case '+':
                    syms.pop();
                    current += num;
                    syms.pop();
                    break;
                }
            }
            else
                current = ch - '0';
            cout << current << endl;
            syms.push('0');
        }
    }
    if (syms.empty()) return 0;
    cout << syms.size() << endl;
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
