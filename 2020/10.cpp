/*
    Advent of Code Day 10

    To run on a mac:

        1. Update makefile "DAY" variable to 10
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/10
*/

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define INPUT_FILE "input10.txt"
#define MAX_JUMP 3

void read_file(vector<int>& nums)
{
    ifstream infile(INPUT_FILE);
    int num;

    // Read file into nums
    while(infile >> num)
    {
        nums.push_back(num);
    }
    infile.close();
}

int part1(vector<int>& nums)
{
    int joltDiffIs1 = 0;
    int joltDiffIs3 = 1; // last jump is 3

    for (int i = 1; i < nums.size(); i++)
    {
        if (nums[i] - nums[i-1] == 3)
            joltDiffIs3 += 1;
        else if (nums[i] - nums[i-1] == 1)
            joltDiffIs1 += 1;
    }
    return joltDiffIs1 * joltDiffIs3;
}

long count_combinations(vector<int>& nums, size_t idx, vector<long>& memo)
{
    if (idx == nums.size()-1) return 1; // if we're at the end
    if (memo[idx] != -1) return memo[idx]; // if we've seen this before

    long count = 0;
    int incr = 1;
    while (idx < nums.size() - incr && // while we're in bounds
           nums[idx + incr] - nums[idx] <= MAX_JUMP) // and we can still jump
    {
        count += count_combinations(nums, idx + incr, memo); // jump
        incr++;
    }

    memo[idx] = count; // got a result, let's save it
    return count;
}

int main(int argc, char *argv[])
{
    vector<int> nums = {0}; // start at 0
    read_file(nums);
    sort(nums.begin(), nums.end());
    vector<long> memo(nums.size(), -1);

    cout << "Part 1: " << part1(nums) << endl;
    cout << "Part 2: " << count_combinations(nums, 0, memo) << endl;

    return 0;
}
