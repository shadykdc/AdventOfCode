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

using namespace std;

#define INPUT_FILE_1 "input19.1.txt"
#define INPUT_FILE_2 "input19.2.txt"

class MapItem
{
private:
public:
    // e.g. 115 24 | 122 36
    int a; // 115
    int b; // 24
    int c; // 122 (or -1)
    int d; // 36 (or -1)
    char ch; // "" (or "a", etc.)
    MapItem() { a = -1; b = -1; c = -1; d = -1; ch = '\0'; }
    MapItem(int _a, int _b, int _c, int _d, char _ch)
    {
        a = _a; b = _b; c = _c; d = _d;
        ch = _ch;
    }
};

void read_file(vector<string>& strs, unordered_map<int, MapItem>& map)
{
    FILE* pfile = fopen(INPUT_FILE_1, "r");
    if (pfile == NULL)
    {
        cerr << "Invalid file" << endl;
        exit(1);
    }

    // I got lazy
    map[24] = MapItem(-1, -1, -1, -1, 'b');
    map[36] = MapItem(-1, -1, -1, -1, 'a');

    ifstream ifs1(INPUT_FILE_1, ifstream::in);
    string str;

    while(ifs1.good())
    {
        getline(ifs1, str);
        std::stringstream ss(str);
        if (str.size() == 0) break;
        int idx;
        int a = -1, b = -1, c = -1, d = -1;
        if (ss >> idx)
        {
            if (ss.peek() == ':')
                ss.ignore();
            if (ss >> a && ss >> b && ss.peek() == '|')
            {
                ss.ignore();
                if (ss >> c)
                    ss >> d;
            }
        }
        map[idx] = MapItem(a, b, c, d, '\0');
    }

    ifs1.close();

    ifstream ifs2(INPUT_FILE_2, ifstream::in);
    while (ifs2.good())
    {
        getline(ifs2, str);
        strs.push_back(str);
    }
    ifs2.close();
    return;
}

int main(int argc, char *argv[])
{
    vector<string> strs;
    unordered_map<int, MapItem> map;
    read_file(strs, map);

    int idx = 126;
    cout << "map[" << idx << "] = " << map[idx].a << " "
    << map[idx].b << " " << map[idx].c << " " << map[idx].d << " "
    << map[idx].ch << "--" << endl;

    return 0;
}
