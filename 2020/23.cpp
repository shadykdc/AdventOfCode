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
#include <unordered_map>

using namespace std;

#define INPUT_FILE "input23.txt"
#define CUPS_TO_MOVE 3
#define MAGIC_CRAB_NUM 1000000

class CupGame
{
private:
    list<long>::iterator current_cup;
    long min_cup_label;
    long max_cup_label;

    // we are about to move these so they're invalid as destinations
    bool invalid_dest(int dest_label)
    {
        bool invalid = false;
        auto check_cup = (*current_cup == cups.back())
            ? cups.begin()
            : next(current_cup);
        for (int i = 0; i < CUPS_TO_MOVE; i++)
        {
            if (dest_label == *check_cup)
                invalid = true;
            check_cup =
                (*check_cup == cups.back())
                ? cups.begin()
                : next(check_cup);
        }
        return invalid;
    };

public:
    list<long> cups;
    unordered_map<long, list<long>::iterator> map;

    CupGame(list<long> _cups, bool _to_a_million)
    {
        cups = _cups;
        min_cup_label = 1;
        auto cup = cups.begin();
        for (auto num : cups)
        {
            map[num] = cup;
            cup = next(cup);
        }
        if (_to_a_million)
        {
            long num = cups.size() + 1;
            while(cups.size() != MAGIC_CRAB_NUM)
            {
                cups.push_back(num);
                map[num] = prev(cups.end());
                num++;
            }
        }
        current_cup = cups.begin();
        max_cup_label = cups.size();
    };

    void Move()
    {
        // step 1 - select a destination cup
        long dest_label = *current_cup - 1;
        while (dest_label < min_cup_label || invalid_dest(dest_label))
        {
            dest_label--;
            if (dest_label < min_cup_label)
                dest_label = max_cup_label;
        }
        auto got = map.find(dest_label);
        if (got == map.end())
            throw("Couldn't find dest_label in map.");
        auto dest_cup =
            (got->first == cups.back())
            ? cups.begin()
            : next(got->second);
        // step 2 - place move cups immediately cw of the destination cup
        // (except splice places things before so... ccw of destination + 1)
        auto move_cup =
            (*current_cup == cups.back())
            ? cups.begin()
            : next(current_cup);
        for (int i = 0; i < CUPS_TO_MOVE; i++)
        {
            cups.splice(dest_cup, cups, move_cup);
            move_cup =
                (*current_cup == cups.back())
                ? cups.begin()
                : next(current_cup);
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
        if (one == map.end())
            throw("couldn't find 1");
        auto print_me =
            (one->first == cups.back())
            ? cups.begin()
            : next(one->second);
        while (print_me != cups.end())
            cout << *print_me++;
        print_me = cups.begin();
        while (*print_me != 1)
            cout << *print_me++;
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
    // cups->Print();
    for (size_t i = 0; i < moves; i++)
    {
        cups->Move();
        // cups->Print();
    }
    cout << "Part 1: ";
    cups->PrintFrom1();
}

void part2(CupGame* cups, size_t moves)
{
    for (size_t i = 0; i < moves; i++)
        cups->Move();
    auto one = cups->map.find(1);
    if (one == cups->map.end())
        throw("couldn't find 1");
    auto two =
        (1 == cups->cups.back())
        ? cups->cups.begin()
        : next(one->second);
    auto three =
        (*two == cups->cups.back())
        ? cups->cups.begin()
        : next(two);
    cout << "Part 2: " << *two * *three << endl;
}

int main(int argc, char *argv[])
{
    list<long> input = {9,4,2,3,8,7,6,1,5};
    CupGame cups1(input, false);
    part1(&cups1, 100); // 36542897
    CupGame cups2(input, true);
    part2(&cups2, 10000000); // 562136730660

    return 0;
}
