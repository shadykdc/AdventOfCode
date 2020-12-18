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

long compute(string equation, size_t start, size_t* end)
{
    stack<char> syms;
    long left_num = 0, right_num = 0;
    char ch;

    for (size_t i = start; i < equation.size(); i++)
    {
        ch = equation[i];
        switch(ch)
        {
        case '+':
        case '*':
            syms.push(ch);
            continue;
        case ')':
            if (end != NULL) *end = i;
            return left_num;
        case '(':
            right_num = compute(equation, i+1, &i);
            break;
        default: // number
            right_num = ch - '0';
        }
        if (syms.size() != 0)
        {
            switch (syms.top())
            {
            case '*':
                left_num *= right_num;
                break;
            case '+':
                left_num += right_num;
                break;
            }
            syms.pop();
            syms.pop();
        }
        else if (right_num)
            left_num = right_num;
        else
            left_num = ch - '0';
        syms.push('0');
    }
    return left_num;
}

long part1(vector<string>& equations)
{
    long count = 0;
    for (auto equation : equations)
    {
        count += compute(equation, 0, NULL);
    }
    return count;
}

int main(int argc, char *argv[])
{
    vector<string> equations;
    read_file(equations);
    cout << "Part 1:\n" << part1(equations) << endl;

    return 0;
}
