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
    vector<strings> strs;
    size_t id;
    char ch;
    MapItem(int _id) { ch = '\0'; id = _id;}
    MapItem(char _ch, int _id) { ch = _ch; id = _id}
};

void read_file(unordered_set<string>& strs, unordered_map<size_t, MapItem>& map)
{
    FILE* pfile = fopen(INPUT_FILE_1, "r");
    if (pfile == NULL)
    {
        cerr << "Invalid file" << endl;
        exit(1);
    }

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
            map[idx] = MapItem('\0', idx);
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

void populate_map_strs(unordered_map<size_t, MapItem>& map, size_t idx)
{
    return;
}

// return the number of messages that completely match rule idx
int part1(unordered_set<string>& strs, unordered_map<int, MapItem>& map, size_t idx)
{
    populate_map_strs(map, idx);

    int count = 0;
    for (auto str : map[idx].strs)
    {
        if (strs.find(str) != strs.end())
            count ++;
    }
    return count;
}

int main(int argc, char *argv[])
{
    unordered_set<string> strs;
    unordered_map<size_t, MapItem> map;

    // I got lazy
    map[24] = MapItem('b', 24);
    map[36] = MapItem('a', 36);

    read_file(strs, map);

    cout << "Part 1: " << part1(strs, map, 0) << endl;

    return 0;
}
