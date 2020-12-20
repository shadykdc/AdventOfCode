/*
    Advent of Code Day 19

    To run on a mac:

        1. Update makefile "DAY" variable to 19
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/19
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <unordered_set>

using namespace std;

#define INPUT_FILE_1 "input19.1.txt"
#define INPUT_FILE_2 "input19.2.txt"

class MapItem
{
private:
public:
    vector<vector<int>> combs;
    char ch;
    MapItem() { ch = '\0'; }
    MapItem(char _ch) { ch = _ch; }
};

void read_file(unordered_set<string>& strs, unordered_map<int, MapItem>& map)
{
    FILE* pfile = fopen(INPUT_FILE_1, "r");
    if (pfile == NULL)
    {
        cerr << "Invalid file" << endl;
        exit(1);
    }

    // I got lazy
    map[24] = MapItem('b');
    map[36] = MapItem('a');

    ifstream ifs1(INPUT_FILE_1, ifstream::in);
    string str;

    while(ifs1.good())
    {
        getline(ifs1, str);
        std::stringstream ss(str);
        if (str.size() == 0) break;
        int idx, num;
        if (ss >> idx)
        {
            if (ss.peek() == ':')
                ss.ignore();
            map[idx] = MapItem('\0');
            vector<int> comb;
            while (ss >> num)
            {
                comb.push_back(num);
                if (ss.peek() == '|')
                {
                    map[idx].combs.push_back(comb);
                    comb.clear();
                    ss.ignore();
                }
            }
            map[idx].combs.push_back(comb);
        }
    }

    ifs1.close();

    ifstream ifs2(INPUT_FILE_2, ifstream::in);
    while (ifs2.good())
    {
        getline(ifs2, str);
        strs.insert(str);
    }
    ifs2.close();
    return;
}

void get_matches(nordered_set<string>& strs, unordered_map<int, MapItem>& map, int idx,
vector<string>& matches, string comb)
{
    string comb;
    if (map[idx].ch != '\0')
    {
        comb += map[idx].ch;
        return;
    }

    for (auto list : map[idx].combs)
    {
        string str;
        for (int i = 0; i < list.size(); i++)
        {
            get_matches(strs, map, list[i], matches, comb);
            str += comb;
        }
    }
    return;
}

// return the number of messages that completely match rule 0
int part1(unordered_set<string>& strs, unordered_map<int, MapItem>& map, int idx)
{
    vector<string> matches;

    get_matches(strs, map, idx, matches, "");

    int count = 0;
    for (auto str : matches)
    {
        if (strs.find(str) != strs.end())
            count ++;
    }
    return count;
}

int main(int argc, char *argv[])
{
    unordered_set<string> strs;
    unordered_map<int, MapItem> map;
    read_file(strs, map);

    cout << "Part 1: " << part1(strs, map, 0) << endl;

    return 0;
}
