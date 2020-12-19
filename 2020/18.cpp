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

long compute1(string equation, size_t start, size_t* end)
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
            right_num = compute1(equation, i+1, &i);
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

long compute2(string equation, size_t start, size_t* end)
{
    if (!equation.size()) return 0;
    char ch;
    vector<int> to_multiply;
    vector<int> to_sum;
    stack<int> nums;
    int sum = 0;
    long prod = 1;
    char last_op;

    for (size_t i = start; i < equation.size(); i++)
    {
        ch = equation[i];
        switch(ch)
        {
        case '+':
            to_sum.push_back(nums.top());
            cout << "pushed " << nums.top() << " to to_sum." << endl;
            nums.pop();
            last_op = '+';
            break;
        case '*':
            if (to_sum.size())
            {
                sum = nums.top();
                nums.pop();
                for (auto num : to_sum) sum += num;
                nums.push(sum);
                to_sum.clear();
                cout << "pushed sum " << sum << " to nums." << endl;
            }
            to_multiply.push_back(nums.top());
            cout << "pushed " << nums.top() << " to to_multiply." << endl;
            nums.pop();
            last_op = '+';
            break;
        case ')':
            if (end != NULL) *end = i;
            goto Exit;
            return prod;
        case '(':
            cout << "new call" << endl;
            nums.push(compute2(equation, i+1, &i));
            cout << "pushed " << nums.top() << " to nums." << endl;
            break;
        default: // number
            nums.push(ch - '0');
            cout << "pushed " << ch - '0' << " to nums." << endl;
        }
    }
Exit:
    if (nums.size() && last_op == '+')
        to_sum.push_back(nums.top());
    else if (nums.size() && last_op == '*')
        to_multiply.push_back(nums.top());

    if (to_sum.size())
    {
        sum = 0;
        for (auto num : to_sum) sum += num;
        to_multiply.push_back(sum);
        cout << "pushed sum " << sum << " to to_multiply." << endl;
    }

    prod = 1;
    for (auto num : to_multiply)
    {
        cout << num << " ";
        prod *= num;
    }
    cout << " = " << prod << endl;

    return prod;
}

long part1(vector<string>& equations)
{
    long count = 0;
    for (auto equation : equations)
    {
        count += compute1(equation, 0, NULL);
    }
    return count;
}

long part2(vector<string>& equations)
{
    long count = 0;
    for (auto equation : equations)
    {
        count += compute2(equation, 0, NULL);
    }
    return count;
}

int main(int argc, char *argv[])
{
    vector<string> equations;
    read_file(equations);
    cout << "Part 1:\n" << part1(equations) << endl;
    cout << "Part 2:\n" << part2(equations) << endl;

    return 0;
}
