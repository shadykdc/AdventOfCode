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
    vector<vector<size_t>> combs;
    vector<string> strs;
    size_t id;
    char ch;
    MapItem() { ch = '\0'; id = 0; }
    MapItem(size_t _id) { ch = '\0'; id = _id; }
    MapItem(char _ch, size_t _id) { ch = _ch; id = _id; }
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
        size_t idx, num;
        if (ss >> idx)
        {
            if (ss.peek() == ':')
                ss.ignore();
            map[idx] = MapItem('\0', idx);
            vector<size_t> comb;
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
    if (map[idx].ch != '\0')
    {
        map[idx].strs.push_back(to_string(map[idx].ch));
        return;
    }

    for (auto nums : map[idx].combs) // 1 3, 3 1
    {
        for (auto num : nums) // 3, 1
        {
            bool new_str = true;;
            size_t size1 = map[idx].strs.size();
            size_t size2 = map[num].strs.size();
            if (!size2)
                populate_map_strs(map, num);
            for (auto str2 : map[num].strs) // "b"
            {
                if (!new_str)
                {
                    for (size_t i = 0; i < size1; i++) // not sure
                    {
                        map[idx].strs[i] += str2;
                    }
                }
                else
                {
                    map[idx].strs.push_back(str2);
                    new_str = false;
                }
            }
        }
    }
    return;
}

// return the number of messages that completely match rule idx
size_t part1(unordered_set<string>& strs, unordered_map<size_t, MapItem>& map, size_t idx)
{
    populate_map_strs(map, idx);
    for (auto item : map)
    {
        cout << item.first << " " << endl;
        for (auto str : item.second.strs)
            cout << str << " ";
        cout << endl;
    }

    size_t count = 0;
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
