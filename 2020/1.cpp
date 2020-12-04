/*
    Advent of Code Day 1

    To run on a mac:

        1. Update makefile "DAY" variable to 1
        2. Run "make"
        3. Run "./aoc"

    Part 1

    The Elves in accounting just need you to fix your expense report (your
    puzzle input); apparently, something isn't quite adding up.

    Specifically, they need you to find the two entries that sum to 2020
    and then multiply those two numbers together.

    For example, suppose your expense report contained the following:

    1721
    979
    366
    299
    675
    1456

    In this list, the two entries that sum to 2020 are 1721 and 299.
    Multiplying them together produces 1721 * 299 = 514579, so the correct
    answer is 514579.

    Of course, your expense report is much larger. Find the two entries that
    sum to 2020; what do you get if you multiply them together?

    Part 2

    The Elves in accounting are thankful for your help; one of them even
    offers you a starfish coin they had left over from a past vacation.

    They offer you a second one if you can find three numbers in your expense
    report that meet the same criteria.

    Using the above example again, the three entries that sum to 2020 are 979,
    366, and 675. Multiplying them together produces the answer, 241861950.

    In your expense report, what is the product of the three entries that sum
    to 2020?
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_set>

using namespace std;

#define INPUT_FILE "input1.txt"

long long part1(
    const vector<int>& expense_report,
    int total,
    int start)
{
    unordered_set<int> expenses;

    // Iterate over our list of expenses
    for (int i = start; i < expense_report.size(); i++)
    {
        auto got = expenses.find(total - expense_report[i]);
        if (got != expenses.end())
            return expense_report[i] * *got;
        expenses.insert(expense_report[i]);
    }

    return -1;
}

long long part2(
    const vector<int>& expense_report,
    int total)
{
    for (int i = 0; i < expense_report.size(); i++)
    {
        int product = part1(expense_report, total - expense_report[i], i + 1);
        if (product != -1)
            return product * expense_report[i];
    }
    return -1;
}

int main(int argc, char *argv[])
{
    ifstream infile(INPUT_FILE);
    vector<int> expense_report;
    int num;

    // Read file into expense_report
    while(infile >> num)
    {
        expense_report.push_back(num);
    }
    infile.close();

    cout << "Part 1: " << part1(expense_report, 2020, 0) << endl; // 259716
    cout << "Part 2: " << part2(expense_report, 2020) << endl; // 120637440

    return 0;
}
