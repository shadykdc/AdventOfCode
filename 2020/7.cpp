/*
    Advent of Code Day 7

    To run on a mac:

        1. Update makefile "DAY" variable to 7
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/7
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define INPUT_FILE "input7.txt"
#define BAGS_CONTAIN " bags contain "

struct BagsOfAColor
{
    int count = 0;
    string color;
};

// parse the next BagsOfAColor info from string "str" at current_pos and push it
// to bags
void insert_next_bag(
    vector<BagsOfAColor>& bags,
    string str,
    size_t* current_pos)
{
    BagsOfAColor bag;
    size_t space_pos = str.find(" ", *current_pos);
    size_t num_length = space_pos - *current_pos;
    bag.count = stoi(str.substr(*current_pos, num_length));
    *current_pos += (num_length + 1); // get to the inner_color
    size_t inner_color_length = str.find(" bag", *current_pos) - *current_pos;
    bag.color = str.substr(*current_pos, inner_color_length);
    bags.emplace_back(bag);
}

// parse the string for BagsOfAColor and put them into the vector "bags".
void inner_bags_str_to_vec(vector<BagsOfAColor>& bags, string str)
{
    // [<num> <inner_color> bag(s),] x N
    size_t comma_pos = str.find(",");
    size_t current_pos = 0;

    while(comma_pos != string::npos)
    {
        insert_next_bag(bags, str, &current_pos);
        current_pos = comma_pos + 2; // get to next number (aka bag)
        comma_pos = str.find(",", current_pos);
    }
    insert_next_bag(bags, str, &current_pos);
}

void read_file(
    unordered_map<string, vector<BagsOfAColor>>& color_to_inner_bags,
    unordered_map<string, unordered_set<string>>& color_to_parent_colors)
{
    ifstream ifs(INPUT_FILE, ifstream::in);
    string str;

    while(ifs.good())
    {
        // sample line: drab lavender bags contain 4 pale turquoise bags,
        // 5 faded lime bags, 2 bright aqua bags.
        getline(ifs, str);

        // <outer_color> bags contain [<num> <inner_color> bags,] x N
        size_t bags_contain_pos = str.find(BAGS_CONTAIN);
        if (bags_contain_pos == string::npos) break;
        string outer_color = str.substr(0, bags_contain_pos);
        size_t contains_start = bags_contain_pos + strlen(BAGS_CONTAIN);
        size_t contains_length = str.size() - 1 - contains_start;
        vector<BagsOfAColor> bags = {};
        string contains_str = str.substr(contains_start, contains_length);

        if (contains_str.find("no other bags") == string::npos)
            inner_bags_str_to_vec(bags, contains_str);

        color_to_inner_bags[outer_color] = bags;

        for (auto bag : bags)
        {
            if (color_to_parent_colors.find(bag.color) == color_to_parent_colors.end())
                color_to_parent_colors[bag.color] = {outer_color};
            else
                color_to_parent_colors[bag.color].insert(outer_color);
        }
    }
    ifs.close();
}

// BFS from input_color to all the possible parents
int part1(
    unordered_map<string, unordered_set<string>>& color_to_parent_colors,
    const string input_color)
{
    unordered_set<string> colors_to_check = {input_color};
    unordered_set<string> checked_colors = {};

    while (colors_to_check.size() > 0)
    {
        string color = *colors_to_check.begin();
        checked_colors.insert(color);
        for (auto parent_color : color_to_parent_colors[color])
        {
            if (checked_colors.find(parent_color) == checked_colors.end())
                colors_to_check.insert(parent_color);
        }
        colors_to_check.erase(color);
    }

    if (checked_colors.find(input_color) != checked_colors.end())
        checked_colors.erase(input_color);

    return checked_colors.size();
}

// DFS for all the possible children of input_color
int part2(
    unordered_map<string, vector<BagsOfAColor>>& color_to_inner_bags,
    const string input_color)
{
    int count = 0;
    for (auto child_bag : color_to_inner_bags[input_color])
    {
        count += (child_bag.count +
            child_bag.count * part2(color_to_inner_bags, child_bag.color));
    }
    return count;
}

int main(int argc, char *argv[])
{
    unordered_map<string, vector<BagsOfAColor>> color_to_inner_bags;
    unordered_map<string, unordered_set<string>> color_to_parent_colors;

    read_file(color_to_inner_bags, color_to_parent_colors);

    cout << "Part 1: "
         << part1(color_to_parent_colors, "shiny gold")
         << endl; // 268

    cout << "Part 2: "
         << part2(color_to_inner_bags, "shiny gold")
         << endl; // 7867

    return 0;
}
