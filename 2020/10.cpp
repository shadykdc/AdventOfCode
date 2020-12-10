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

int count_combinations(vector<int>& nums, size_t idx)
{
    if (idx == nums.size()-1) return 1;
    int count = 0;
    // int incr = 1;
    // while (nums[idx + incr] - nums[idx] == 0) incr++;
    // while (idx + incr < nums.size() - incr &&
    //        nums[idx + incr] - nums[idx] <= 3)
    // {
    //     count += count_combinations(nums, idx + incr);
    //     incr++;
    // }

    if (idx < nums.size() - 1 && nums[idx + 1] - nums[idx] <= 3)
        count += count_combinations(nums, idx + 1);
    if (idx < nums.size() - 2 && nums[idx + 2] - nums[idx] <= 3)
        count += count_combinations(nums, idx + 2);
    if (idx < nums.size() - 3 && nums[idx + 3] - nums[idx] <= 3)
        count += count_combinations(nums, idx + 3);
    return count;
}

int part2(vector<int>& nums)
{
    return count_combinations(nums, 0);
}

int main(int argc, char *argv[])
{
    vector<int> nums;
    read_file(nums);
    nums.push_back(0); // start at 0
    sort(nums.begin(), nums.end());

    cout << "Part 1: " << part1(nums) << endl;
    cout << "Part 2: " << part2(nums) << endl;

    return 0;
}
