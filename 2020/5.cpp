/*
    Advent of Code Day 5

    To run on a mac:

        1. Update makefile "DAY" variable to 5
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/5
*/


#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define INPUT_FILE "input5.txt"
#define ROW_MAX_IDX 127 // row is between 0 and 127, inclusive
#define COL_MAX_IDX 7 // col is between 0 and 7, inclusive
#define ROW_CHAR_COUNT 7 // first seven letters in string are F or B
#define COL_CHAR_COUNT 3 // last three letters in string are R or L

// basically a binary search
int get_seat_id(string input)
{
    int row_high = ROW_MAX_IDX;
    int row_low = 0;
    int col_high = COL_MAX_IDX;
    int col_low = 0;

    for (int i = 0; i < ROW_CHAR_COUNT; i++)
    {
        if (input[i] == 'F') // lower half
        {
            row_high = (row_high - row_low)/2 + row_low;
        }
        else if (input[i] == 'B') // upper half
        {
            row_low = (row_high - row_low)/2 + row_low + 1;
        }
        else // input error
        {
            cout << "Bad input." << endl;
            exit(1);
        }
    }

    for(int i = ROW_CHAR_COUNT; i < ROW_CHAR_COUNT + COL_CHAR_COUNT; i++)
    {
        if (input[i] == 'L') // lower half
        {
            col_high = (col_high - col_low)/2 + col_low;
        }
        else if (input[i] == 'R') // upper half
        {
            col_low = (col_high - col_low)/2 + col_low + 1;
        }
        else // input error
        {
            cout << "Bad input." << endl;
            exit(1);
        }
    }

    return row_high * 8 + col_high;
}

void read_input_file(vector<string>& inputs)
{
    string input;
    ifstream ifs(INPUT_FILE, ifstream::in);

    while(ifs.good())
    {
        getline(ifs, input);
        if (input.size() > 0)
            inputs.push_back(input);
    }
    ifs.close();
}

int main(int argc, char *argv[])
{
    vector<string> inputs;

    read_input_file(inputs);

    int max_id = -1;
    int min_id = INT_MAX;
    int sum_of_ids = 0;
    vector<int> seat_ids;
    for (auto input : inputs)
    {
        int seat_id = get_seat_id(input);
        max_id = max(max_id, seat_id);
        min_id = min(min_id, seat_id);
        sum_of_ids += seat_id;
        seat_ids.push_back(seat_id);
    }
    cout << "Part 1: " << max_id << endl; // 963

    // Part 2: This is the theoretical sum from min_id to max_id so the classic
    // "add the numbers from 1 to 100" type problem followed by the "find the
    // missing number in a list of contiguous numbers" problem where you
    // take the sum of 1 to 100 and subtract the sum of the numbers in your
    // list and you end up with the missing number.
    int theoretical_sum = (max_id * (max_id+1) /2) - ((min_id - 1) * min_id/2);
    cout << "Part 2: " << theoretical_sum - sum_of_ids << endl; // 592

    return 0;
}
