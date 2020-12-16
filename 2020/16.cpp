/*
    Advent of Code Day 16

    To run on a mac:

        1. Update makefile "DAY" variable to 16
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/16
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <unordered_map>

using namespace std;

#define INPUT_FILE1 "input16.1.txt"
#define INPUT_FILE2 "input16.2.txt"

struct Range
{
    int end;
    string name;
};

void read_file1(vector<vector<int>>& tickets)
{
    ifstream ifs(INPUT_FILE1, ifstream::in);
    string str;
    size_t ticket_num = 0;

    while(ifs.good())
    {
        getline(ifs, str);
        std::stringstream ss(str);
        if (str.size() == 0) break;
        tickets.push_back({});
        for (int val; ss >> val;)
        {
            tickets[ticket_num].push_back(val);
            if (ss.peek() == ',') ss.ignore();
        }
        ticket_num++;
    }

    ifs.close();
    return;
}

void read_file2(unordered_map<int, Range>& rules)
{
    ifstream ifs(INPUT_FILE2, ifstream::in);
    string str;
    int n1, n2, n3, n4;

    while(ifs.good())
    {
        getline(ifs, str);
        Range range;
        if (str.find(':') == string::npos) break;
        range.name = str.substr(0, str.find(':'));
        string nums =  str.substr(str.find(':') + 2);
        if (sscanf(&nums[0], "%d-%d or %d-%d", &n1, &n2, &n3, &n4) != 4) break;
        range.end = n2;
        rules[n1] = range;
        range.end = n4;
        rules[n3] = range;
    }

    ifs.close();
}

bool invalid(int field, unordered_map<int, Range>& rules)
{
    for (auto item : rules)
    {
        if (field >= item.first && field <= item.second.end)
            return false;
    }
    return true;
}

int part1(vector<vector<int>>& tickets, unordered_map<int, Range>& rules)
{
    int sum = 0;
    for (int i = 0; i < tickets.size(); i++)
    {
        bool invalid_ticket = false;
        for (int j = 0; j < tickets[0].size(); j++)
        {
            int field = tickets[i][j];
            if (invalid(field, rules))
            {
                sum += field; // Part 1
                invalid_ticket = true;
            }
        }
        // Put this here for Part 2 while leaving Part 1 unaffected
        if (invalid_ticket)
        {
            tickets.erase(tickets.begin()+i);
            i--;
        }
    }
    return sum;
}

int part2()
{
    return 1;
}

int main(int argc, char *argv[])
{
    vector<vector<int>> tickets;
    unordered_map<int, Range> rules;

    read_file1(tickets); // 32842
    read_file2(rules);

    cout << part1(tickets, rules) << endl;
    // vector<int> my_ticket = {157,59,163,149,83,131,107,89,109,113,151,53,127,97,79,103,101,173,167,61};
    vector<int> my_ticket = {11,12,13};
    cout << part2() << endl;

    return 0;
}
