/*
    Advent of Code Day 4

    To run on a mac:

        1. Update makefile "DAY" variable to 4
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/4
*/


#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>

using namespace std;

#define INPUT_FILE "input4.txt"

const vector<string> required_fields =
    {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};
const unordered_set<string> valid_eye_colors =
    {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};


// make sure stoi gets a valid string and then check the number is between
// or equal to low and high
bool is_num_in_range(string str, int low, int high)
{
    for (char c : str)
    {
        if (!isdigit(c))
            return false;
    }
    int num = stoi(str);
    if (num >= low && num <= high)
        return true;
    return false;
}

bool data_is_valid(string req_field, string value)
{
    if (strcmp(req_field.c_str(), "byr") == 0)
    {
        return is_num_in_range(value, 1920, 2002);
    }
    else if (strcmp(req_field.c_str(), "iyr") == 0)
    {
        return is_num_in_range(value, 2010, 2020);
    }
    else if (strcmp(req_field.c_str(), "eyr") == 0)
    {
        return is_num_in_range(value, 2020, 2030);
    }
    else if (strcmp(req_field.c_str(), "hgt") == 0)
    {
        if (value.size() == 5)
            return (is_num_in_range(value.substr(0, 3), 150, 193) &&
                    value[3] == 'c' && value[4] == 'm');
        else if (value.size() == 4)
            return (is_num_in_range(value.substr(0, 2), 59, 76) &&
                    value[2] == 'i' && value[3] == 'n');
        return false;
    }
    else if (strcmp(req_field.c_str(), "hcl") == 0)
    {
        if (value.size() > 7 || value.size() < 7)
            return false;
        if (value[0] != '#')
            return false;
        for (char c : value.substr(1))
        {
            if (!isdigit(c) && (c > 'f' || c < 'a'))
                return false;
        }
        return true;
    }
    else if (strcmp(req_field.c_str(), "ecl") == 0)
    {
        auto got = valid_eye_colors.find(value);
        return (got != valid_eye_colors.end());
    }
    else if (strcmp(req_field.c_str(), "pid") == 0)
    {
        if (value.size() != 9)
            return false;
        for (char c : value)
        {
            if (!isdigit(c))
                return false;
        }
        return true;
    }
    else if (strcmp(req_field.c_str(), "cid") == 0)
    {
        return true;
    }
    return false;
}

// return true if all required fields exist and their data is valid
bool is_valid_passport(unordered_map<string, string>& passport)
{
    for (auto req_field : required_fields)
    {
        auto got = passport.find(req_field);
        bool field_not_found = got == passport.end();
        // comment out the data_is_valid call for Part 1
        if (field_not_found || !data_is_valid(req_field, got->second))
            return false;
    }
    return true;
}

int count_valid_passports(
    const vector<unordered_map<string, string>>& passports)
{
    // count valid passports
    int count = 0;
    for (auto passport : passports)
    {
        if (is_valid_passport(passport))
            count++;
    }
    return count;
}

void read_file(vector<unordered_map<string, string>>& passports)
{
    ifstream ifs(INPUT_FILE);
    string str;
    passports.push_back({});
    while(ifs >> str)
    {
        passports.back()[str.substr(0, 3)] = str.substr(4);
        if (ifs.peek() == '\n')
        {
            ifs.get();
            if (ifs.peek() == '\n')
                passports.push_back({});
        }
    }
    ifs.close();
    passports.pop_back();
}

int main(int argc, char *argv[])
{
    vector<unordered_map<string,string>> passports;

    read_file(passports);

    cout << "Number of valid passports: "
         << count_valid_passports(passports)
         << endl;
    // Part 1: 202
    // Part 2: 137

    return 0;
}
