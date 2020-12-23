/*
    Advent of Code Day 23

    To run on a mac:

        1. Update makefile "DAY" variable to 23
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/23
*/

#include <iostream>
#include <fstream>
#include <list>
#include <algorithm>
#include <iterator>
#include <vector>
#include <unordered_map>

using namespace std;

#define INPUT_FILE "input23.txt"

class CupGame
{
public:
    list<long> cups;
    list<long>::iterator current_cup;
    unordered_map<long, list<long>::iterator> map;
    long min_cup_label;
    long max_cup_label;
    CupGame(list<long> _cups, bool to_a_million)
    {
        cups = _cups;
        min_cup_label = LONG_MAX;
        max_cup_label = LONG_MIN;
        current_cup = cups.begin();

        auto cup = cups.begin();
        for (auto num : cups)
        {
            map[num] = cup;
            cup = next(cup);
        }
        if (to_a_million)
        {
            long num = cups.size() + 1;
            while(cups.size() != 1000000)
            {
                cups.push_back(num);
                map[num] = cup;
                cup = next(cup);
                num++;
            }
        }
        for (auto cup : cups)
        {
            min_cup_label = min(min_cup_label, cup);
            max_cup_label = max(max_cup_label, cup);
        }
    };
    void Move()
    {
        // step 1 - get three cups
        vector<long> three_cups = {};
        while (three_cups.size() < 3)
        {
            list<long>::iterator next_node =
                ( *current_cup == cups.back() )
                ? cups.begin()
                : next(current_cup);
            three_cups.push_back(*next_node);
            map.erase(*next_node);
            cups.erase(next_node);
        }
        // step 2 - select a destination cup
        long dest_label = *current_cup - 1;
        auto got = map.find(dest_label);
        while (got == map.end())
        {
            dest_label--;
            if (dest_label < min_cup_label)
                dest_label = max_cup_label;
            got = map.find(dest_label);
        }
        // step 3 - place cups immediately cw of dest_idx
        auto next_cup = (dest_label == cups.back()) ? cups.begin() : next(got->second);
        cups.insert(next_cup, three_cups.begin(), three_cups.end());
        list<long>::iterator dest = got->second;
        for (size_t i = 0; i < 3; i++)
        {
            dest = (*dest == cups.back() ) ? cups.begin() : next(dest);
            map[*dest] = dest;
        }
        // step 4 - get next cup
        current_cup =
                ( *current_cup == cups.back() )
                ? cups.begin()
                : next(current_cup);
    };
    void PrintFrom1()
    {
        auto one = map.find(1);
        if (one == map.end()) cout << "couldn't find 1" << endl;
        auto print_me = next(one->second);
        while (print_me != cups.end())
        {
            cout << *print_me;
            print_me++;
        }
        print_me = cups.begin();
        while (*print_me != 1)
        {
            cout << *print_me;
            print_me++;
        }
        cout << endl;
    };

    void Print()
    {
        for (auto cup = cups.begin(); cup != cups.end(); cup++)
        {
            if (*cup == *current_cup) cout << "(" << *cup << ") ";
            else cout << *cup << " ";
        }
        cout << endl;
    };
};

void part1(CupGame* cups, size_t moves)
{
    cups->Print();
    for (size_t i = 0; i < moves; i++)
    {
        cups->Move();
        cups->Print();
    }
    cout << "Part 1: ";
    cups->PrintFrom1();
    cout << endl;
}

void part2(CupGame* cups, size_t moves)
{
    for (size_t i = 0; i < moves; i++)
        cups->Move();

    auto one = cups->map.find(1);
    if (one == cups->map.end()) cout << "couldn't find 1" << endl;
    auto two = (1 == cups->cups.back()) ? cups->cups.begin() : next(one->second);
    auto three = (*two == cups->cups.back()) ? cups->cups.begin() : next(two);
    cout << *two * *three << endl;
}

int main(int argc, char *argv[])
{
    CupGame cups1({9,4,2,3,8,7,6,1,5}, false); // my input
    // CupGame cups1({3,8,9,1,2,5,4,6,7}, false); // example
    part1(&cups1, 100); // 36542897
    CupGame cups2({9,4,2,3,8,7,6,1,5}, true);
    // part2(&cups2, 10000000); //
    cout << endl;

    return 0;
}
