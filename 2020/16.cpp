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
#include <queue>

using namespace std;

#define INPUT_FILE1 "input16.1.txt"
#define INPUT_FILE2 "input16.2.txt"
#define INIT_INDEX -2

struct FieldRule
{
    int start1;
    int end1;
    int start2;
    int end2;
    int index;
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

void read_file2(vector<FieldRule>& rules)
{
    ifstream ifs(INPUT_FILE2, ifstream::in);
    string str;

    while(ifs.good())
    {
        getline(ifs, str);
        FieldRule rule;
        rule.index = INIT_INDEX;
        if (str.find(':') == string::npos) break;
        rule.name = str.substr(0, str.find(':'));
        string nums =  str.substr(str.find(':') + 2);
        if (sscanf(&nums[0], "%d-%d or %d-%d",
            &rule.start1, &rule.end1, &rule.start2, &rule.end2) != 4) break;
        rules.push_back(rule);
    }

    ifs.close();
}

bool invalid(int field, vector<FieldRule>& rules)
{
    for (auto rule : rules)
    {
        if ((field >= rule.start1 && field <= rule.end1) ||
            (field >= rule.start2 && field <= rule.end2))
            return false;
    }
    return true;
}

int part1(vector<vector<int>>& tickets, vector<FieldRule>& rules)
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

long long get_result(vector<FieldRule>& rules, vector<int>& my_ticket)
{
    long long result = 1;
    for (auto rule : rules)
    {
        if (rule.name.substr(0, strlen("departure")).compare("departure") == 0)
            result *= my_ticket[rule.index];
    }
    return result;
}

bool valid_for_all_tickets(vector<vector<int>>& tickets, int idx, FieldRule* rule)
{
    for (auto ticket : tickets)
    {
        int field = ticket[idx];
        if (!((field >= rule->start1 && field <= rule->end1) ||
              (field >= rule->start2 && field <= rule->end2)))
        {
            return false;
        }
    }
    return true;
}

bool dfs(vector<vector<int>>& tickets, vector<FieldRule>& rules, queue<int>& indices)
{
    if (indices.size() == 0)
        return true;

    for (int j = 0 ; j < rules.size(); j++)
    {
        FieldRule* rule = &rules[j];
        if (rule->index != INIT_INDEX) continue;
        for (int i = 0; i < indices.size(); i++)
        {
            int idx = indices.front();
            indices.pop();
            if (valid_for_all_tickets(tickets, idx, rule))
            {
                rule->index = idx;
                if (dfs(tickets, rules, indices))
                    return true;
                rule->index = INIT_INDEX;
            }
            indices.push(idx);
        }
    }
    return false;
}

long long part2(vector<vector<int>>& tickets, vector<FieldRule>& rules, vector<int>& my_ticket)
{
    // assign index within rules to correct values
    queue<int> indices;
    for (int i = 0; i < my_ticket.size(); i++)
    {
        indices.push(i);
    }

    dfs(tickets, rules, indices);

    for (auto id : rules) cout << id.index << " "; cout << endl;

    return get_result(rules, my_ticket);
}

int main(int argc, char *argv[])
{
    vector<vector<int>> tickets;
    vector<FieldRule> rules;

    read_file1(tickets); // 32842
    read_file2(rules);

    cout << part1(tickets, rules) << endl;
    vector<int> my_ticket = {157,59,163,149,83,131,107,89,109,113,151,53,127,97,79,103,101,173,167,61};
    cout << part2(tickets, rules, my_ticket) << endl;

    return 0;
}
