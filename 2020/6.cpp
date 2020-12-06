/*
    Advent of Code Day 6

    To run on a mac:

        1. Update makefile "DAY" variable to 6
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/6
*/


#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>

using namespace std;

#define INPUT_FILE "input6.txt"

struct Group
{
    unordered_map<char, int> question_to_yes_count;
    int size = 0;
};

int part1(vector<Group>& groups)
{
    int sum = 0;
    for (auto group : groups)
    {
        sum += group.question_to_yes_count.size();
    }
    return sum;
}

int part2(vector<Group>& groups)
{
    int sum = 0;
    for (auto group : groups)
    {
        for (auto got : group.question_to_yes_count)
        {
            // everyone in group said yes to this (got.first) question
            if (group.size == got.second)
                sum++;
        }
    }
    return sum;
}

void read_file(
    vector<Group>& groups)
{
    ifstream ifs(INPUT_FILE);
    string str;
    Group new_group;
    groups.push_back(new_group);
    while(ifs >> str)
    {
        Group* group = &groups.back();
        for (auto c : str)
        {
            auto got = group->question_to_yes_count.find(c);
            if (got != group->question_to_yes_count.end())
                group->question_to_yes_count[c] += 1;
            else
                group->question_to_yes_count[c] = 1;
        }
        group->size++;

        if (ifs.peek() == '\n')
        {
            ifs.get();
            if (ifs.peek() == '\n')
                groups.push_back(new_group);
        }
    }
    ifs.close();
    if (groups.back().size == 0)
        groups.pop_back();
}

int main(int argc, char *argv[])
{
    vector<Group> groups;

    // read file into nums
    read_file(groups);

    cout << "Part 1: " << part1(groups) << endl; // 6775
    cout << "Part 2: " << part2(groups) << endl; // 3356

    return 0;
}
