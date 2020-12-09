/*
    Advent of Code Day 9

    To run on a mac:

        1. Update makefile "DAY" variable to 9
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/9
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_set>

using namespace std;

#define INPUT_FILE "input9.txt"
#define PREAMBLE_SIZE 25

void read_file(vector<long>& data)
{
    ifstream infile(INPUT_FILE);
    long num;

    // Read file into data
    while(infile >> num)
    {
        data.push_back(num);
    }
    infile.close();
}

long get_first_invalid_num(const vector<long>& data)
{
    size_t i = PREAMBLE_SIZE;

    while (i < data.size())
    {
        unordered_set<long> preamble;
        size_t j = i - 1;
        bool found = false;
        while (j >= i - PREAMBLE_SIZE)
        {
            if (preamble.find(data[i] - data[j]) != preamble.end())
            {
                found = true;
                break;
            }
            preamble.insert(data[j]);
            j--;
        }
        if (!found) return data[i];
        i++;
    }
    return -1;
}

long part2(const vector<long>& data, const long target)
{
    int i = 0;
    int j = 1;
    long sum = data[i] + data[j];

    while(i < data.size() && j < data.size())
    {
        if (sum == target)
        {
            // went for saving space over time in this instance
            long min_num = LONG_MAX;
            long max_num = LONG_MIN;
            for (size_t idx = i; idx <= j; idx++)
            {
                min_num = min(min_num, data[idx]);
                max_num = max(max_num, data[idx]);
            }
            return min_num + max_num;
        }
        else if (sum < target)
        {
            j++;
            sum += data[j];
        }
        else if (sum > target)
        {
            sum -= data[i];
            i++;
        }
    }
    return -1;
}

int main(int argc, char *argv[])
{
    vector<long> data;
    read_file(data);

    long invalid_num = get_first_invalid_num(data);
    cout << "Part 1: " << invalid_num << endl; // 530627549
    cout << "Part 2: " << part2(data, invalid_num) << endl;

    return 0;
}
