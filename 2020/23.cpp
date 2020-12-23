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

using namespace std;

#define INPUT_FILE "input23.txt"

class CupGame
{
public:
    list<int> cups;
    list<int>::iterator current_cup;
    int min_cup_label;
    int max_cup_label;
    CupGame(list<int> _cups, bool to_a_million)
    {
        cups = _cups;
        min_cup_label = INT_MAX;
        max_cup_label = INT_MIN;
        for (auto cup : cups)
        {
            min_cup_label = min(min_cup_label, cup);
            max_cup_label = max(max_cup_label, cup);
        }
        current_cup = cups.begin();
        if (to_a_million)
        {
            int num = cups.size() + 1;
            while(cups.size() != 1000000)
            {
                cups.push_back(num);
                num++;
            }
        }
    };
    void Move()
    {
        // step 1 - get three cups
        vector<int> three_cups = {};
        while (three_cups.size() < 3)
        {
            list<int>::iterator next_node =
                ( *current_cup == cups.back() )
                ? cups.begin()
                : next(current_cup);
            three_cups.push_back(*next_node);
            cups.erase(next_node);
        }
        cout << "pick up ";
        for (auto cup : three_cups) cout << cup << " ";
        cout << endl;
        // step 2 - select a destination cup
        int dest_label = *current_cup - 1;
        auto got = find(cups.begin(), cups.end(), dest_label);
        while (got == cups.end())
        {
            dest_label--;
            if (dest_label < min_cup_label)
                dest_label = max_cup_label;
            got = find(cups.begin(), cups.end(), dest_label);
        }
        cout << "destination: " << dest_label << endl;
        // step 3 - place cups immediately cw of dest_idx
        auto next_cup = (*got == cups.back()) ? cups.begin() : next(got);
        cups.insert(next_cup, three_cups.begin(), three_cups.end());
        // step 4 - find idx of number in front of current_label
        current_cup =
                ( *current_cup == cups.back() )
                ? cups.begin()
                : next(current_cup);
    };

    void PrintFrom1()
    {
        // find 1
        auto one = find(cups.begin(), cups.end(), 1);
        if (one == cups.end()) return;
        auto print_me = (*one == cups.back()) ? cups.begin() : next(one);
        while (print_me != cups.end())
        {
            cout << *print_me;
            print_me++;
        }
        print_me = cups.begin();
        while (*print_me != *one)
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

void part1(CupGame* cups, int moves)
{
    cups->Print();
    for (int i = 0; i < moves; i++)
    {
        cups->Move();
        cups->Print();
    }
    cout << "Part 1: ";
    cups->PrintFrom1();
    cout << endl;
}

void part2(CupGame* cups, int moves)
{
    for (int i = 0; i < moves; i++)
    {
        cups->Move();
    }
    // find 1
    auto one = find(cups->cups.begin(), cups->cups.end(), 1);
    auto two =   (*one == cups->cups.back()) ? cups->cups.begin() : next(one);
    auto three = (*two == cups->cups.back()) ? cups->cups.begin() : next(two);
    cout << *two * *three << endl;
}

int main(int argc, char *argv[])
{
    CupGame cups1({9,4,2,3,8,7,6,1,5}, false);
    // CupGame cups1({3,8,9,1,2,5,4,6,7}, false);
    part1(&cups1, 100); // 36542897
    CupGame cups2({9,4,2,3,8,7,6,1,5}, true);
    // part2(&cups2, 10000000); //
    cout << endl;

    return 0;
}
