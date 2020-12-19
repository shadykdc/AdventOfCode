/*
    Advent of Code Day 17

    To run on a mac:

        1. Update makefile "DAY" variable to 17
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/17
*/

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define INPUT_FILE "input17.txt"
#define CYCLES 6

class Point
{
    int x, y, z, w;
public:
    Point(int x, int y, int z, int w);
    bool operator==(const Point &p) const
    {
        return x == p.x && y == p.y && z == p.z && w == p.w;
    }
    bool is_neighbor(int _x, int _y, int _z, int _w)
    {
        return abs(x - _x) <= 1 && abs(y - _y) <= 1 &&
               abs(z - _z) <= 1 && abs(w - _w) <= 1;
    }
};

Point::Point(int _x, int _y, int _z, int _w)
{
    x = _x;
    y = _y;
    z = _z;
    w = _w;
}

class Space
{
private:
    // too lazy to make hash function to make this a set and be faster
    vector<Point> active_pts = {};
public:
    Space();
    int z_min, z_max, x_min, x_max, y_min, y_max, w_min, w_max;
    bool activate_pt(int x, int y, int z, int w);
    bool deactivate_pt(int x, int y, int z, int w);
    bool pt_is_active(int x, int y, int z, int w);
    size_t count_active_nearby(int x, int y, int z, int w);
    size_t get_active_count() { return active_pts.size(); }
};

Space::Space()
{
    vector<Point> active_pts = {};
    z_min = 0;
    z_max = 0;
    x_min = 0;
    x_max = 0;
    y_min = 0;
    y_max = 0;
    w_min = 0;
    w_max = 0;
}

// returns false if point already existed
bool Space::activate_pt(int x, int y, int z, int w)
{
    if (pt_is_active(x, y, z, w)) return false;
    Point p(x, y, z, w);
    active_pts.push_back(p);
    x_min = min(x_min, x);
    x_max = max(x_max, x);
    y_min = min(y_min, y);
    y_max = max(y_max, y);
    z_min = min(z_min, z);
    z_max = max(z_max, z);
    w_min = min(w_min, w);
    w_max = max(w_max, w);
    return true;
}

bool Space::pt_is_active(int x, int y, int z, int w)
{
    Point p(x, y, z, w);
    for (auto point : active_pts)
    {
        if (point == p) return true;
    }
    return false;
}

// returns false if point didn't exist
bool Space::deactivate_pt(int x, int y, int z, int w)
{
    Point p(x, y, z, w);
    for (int i = 0; i < active_pts.size(); i++)
    {
        if (active_pts[i] == p)
        {
            active_pts.erase(active_pts.begin()+i);
            return true;
        }
    }
    return false;
}

size_t Space::count_active_nearby(int px, int py, int pz, int pw)
{
    size_t count = 0;
    for (int x = px-1; x <= px+1; x++)
    {
        for (int y = py-1; y <= py+1; y++)
        {
            for (int z = pz-1; z <= pz+1; z++)
            {
                for (int w = pw-1; w <= pw+1; w++)
                {
                    if (x == px && y == py && z == pz && w == pw )
                        continue;
                    if (pt_is_active(x, y, z, w))
                        count++;
                }
            }
        }
    }
    return count;
}

void read_file(vector<string>& grid, Space* space)
{
    string row;
    ifstream ifs(INPUT_FILE, ifstream::in);

    while(ifs.good())
    {
        getline(ifs, row);
        if (row.size() > 0)
            grid.push_back(row);
    }
    ifs.close();

    for (int y = 0; y < grid.size(); y++)
    {
        for (int x = 0; x < grid[0].size(); x++)
        {
            if (grid[y][x] == '#')
            {
                space->activate_pt(x, y, 0, 0);
            }
        }
    }

    return;
}

void iterate(Space* space)
{
    Space new_space = *space;
    for (int x = space->x_min-1; x <= space->x_max+1; x++)
    {
        for (int y = space->y_min-1; y <= space->y_max+1; y++)
        {
            for (int z = space->z_min-1; z <= space->z_max+1; z++)
            {
                for (int w = space->w_min-1; w <= space->w_max+1; w++)
                {
                    size_t count = space->count_active_nearby(x, y, z, w);
                    if (space->pt_is_active(x, y, z, w))
                    {
                        if (count != 2 && count != 3)
                            new_space.deactivate_pt(x, y, z, w);
                    }
                    else if (count == 3)
                        new_space.activate_pt(x, y, z, w);
                }
            }
        }
    }
    *space = new_space;
}

int part2(Space* space)
{
    for (int i = 0; i < CYCLES; i++)
        iterate(space);
    return space->get_active_count();
}

int main(int argc, char *argv[])
{
    vector<string> grid;
    Space space;

    read_file(grid, &space);

    cout << "Part 2: " << part2(&space) << endl; // 2460

    return 0;
}
