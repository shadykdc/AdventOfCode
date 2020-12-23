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
#include <vector>

using namespace std;

#define INPUT_FILE "input23.txt"

class CupGame
{
public:
    vector<int> cups;
    int current_idx;
    int current_label;
    int min_cup_label;
    int max_cup_label;
    CupGame(vector<int> _cups, bool to_a_million)
    {
        cups = _cups;
        min_cup_label = INT_MAX;
        max_cup_label = INT_MIN;
        for (auto cup : cups)
        {
            min_cup_label = min(min_cup_label, cup);
            max_cup_label = max(max_cup_label, cup);
        }
        current_idx = 0;
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
        current_label = cups[current_idx];
        // step 1 - get three cups
        vector<int> three_cups;
        int idx = (current_idx + 1) % cups.size();
        while (three_cups.size() < 3)
        {
            three_cups.push_back(cups[idx]);
            cups.erase(cups.begin() + idx);
            // remember cups size changes in this loop
            for (int i = 0; i < cups.size(); i++)
            {
                if (cups[i] == current_label)
                    current_idx = i;
            }
            idx = (current_idx + 1) % cups.size();
        }
        // step 2 - select a destination cup
        int dest_label = cups[current_idx];
        int dest_idx = -1;
        while (dest_idx == -1)
        {
            dest_label--;
            if (dest_label < min_cup_label)
                dest_label = max_cup_label;
            for (int i = 0; i < cups.size(); i++)
            {
                if (cups[i] == dest_label)
                {
                    dest_idx = i + 1;
                    break;
                }
            }
        }
        // step 3 - place cups immediately cw of dest_idx
        cups.insert(cups.begin() + dest_idx, three_cups.begin(), three_cups.end());
        // step 4 - find idx of number in front of current_label
        for (int i = 0; i < cups.size(); i++)
        {
            if (cups[i] == current_label)
            {
                current_idx = (i + 1) % cups.size();
                break;
            }
        }
    };

    void PrintFrom1()
    {
        // find 1
        int idx_of_one = -1;
        for (int i = 0; i < cups.size(); i++)
        {
            if (cups[i] == 1)
                idx_of_one = i;
        }

        for (int i = idx_of_one + 1; i < (cups.size() + idx_of_one - 1); i++)
        {
            int j = i % cups.size();
            cout << cups[j];
        }
        cout << endl;
    };

    void Print()
    {
        for (int i = 0; i < cups.size(); i++)
        {
            if (i == current_idx) cout << "(" << cups[i] << ") ";
            else cout << cups[i] << " ";
        }
        cout << endl;
    };
};

void part1(CupGame* cups, int moves)
{
    // cups->Print();
    for (int i = 0; i < moves; i++)
    {
        cups->Move();
        // cups->Print();
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
    int idx_of_one = -1;
    for (int i = 0; i < cups->cups.size(); i++)
    {
        if (cups->cups[i] == 1)
            idx_of_one = i;
    }
    cout << cups->cups[ (idx_of_one + 1) % cups->cups.size() ] *
            cups->cups[ (idx_of_one + 2) % cups->cups.size() ]
         << endl;
}

int main(int argc, char *argv[])
{
    CupGame cups1({9,4,2,3,8,7,6,1,5}, false);
    part1(&cups1, 100); // 36542897
    CupGame cups2({9,4,2,3,8,7,6,1,5}, true);
    part2(&cups2, 10000000); //
    cout << endl;

    return 0;
}
