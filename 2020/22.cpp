/*
    Advent of Code Day 22

    To run on a mac:

        1. Update makefile "DAY" variable to 22
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/22
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <deque>
#include <sstream>
#include <unordered_set>

using namespace std;

#define INPUT_FILE "input22.txt"

void read_file(deque<int>& player1, deque<int>& player2)
{
    ifstream ifs(INPUT_FILE);
    int num;
    string str;

    if(ifs.good())
    {
        getline(ifs, str);
        stringstream ss(str);
        while (ss >> num)
            player1.push_back(num);
    }
    if(ifs.good())
    {
        getline(ifs, str);
        stringstream ss(str);
        while (ss >> num)
            player2.push_back(num);
    }
    ifs.close();

    return;
}

int get_score(deque<int>& player)
{
    int sum = 0;
    while(player.size())
    {
        sum += player.front() * player.size();
        player.pop_front();
    }
    return sum;
}

int part1(deque<int>& player1, deque<int>& player2)
{
    while (player1.size() && player2.size())
    {
        int card1 = player1.front();
        int card2 = player2.front();
        player1.pop_front();
        player2.pop_front();
        if (card1 > card2)
        {
            player1.push_back(card1);
            player1.push_back(card2);
        }
        else if (card2 > card1)
        {
            player2.push_back(card2);
            player2.push_back(card1);
        }
    }

    if (player1.size()) return get_score(player1);
    return get_score(player2);
}

bool seen_before(deque<int>& player1, deque<int>& player2,
    unordered_set<string>& seen)
{
    string str = "1";
    for (auto num : player1)
        str += to_string(num);
    if (seen.find(str) != seen.end())
        return true;
    str = "2";
    for (auto num : player2)
        str += to_string(num);
    if (seen.find(str) != seen.end())
        return true;
    seen.insert(str);
    return false;
}

bool player1Wins(deque<int>& player1, deque<int>& player2)
{
    unordered_set<string> seen;

    while (player1.size() && player2.size())
    {
        if (seen_before(player1, player2, seen))
            return true;
        int card1 = player1.front();
        int card2 = player2.front();
        player1.pop_front();
        player2.pop_front();

        if (card1 <= player1.size() && card2 <= player2.size())
        {
            deque<int> p1(player1.begin(), player1.begin() + card1);
            deque<int> p2(player2.begin(), player2.begin() + card2);
            if (player1Wins(p1, p2))
            {
                player1.push_back(card1);
                player1.push_back(card2);
                continue;
            }
            player2.push_back(card2);
            player2.push_back(card1);
        }
        else if (card1 > card2)
        {
            player1.push_back(card1);
            player1.push_back(card2);
        }
        else // card2 >= card1
        {
            player2.push_back(card2);
            player2.push_back(card1);
        }
    }
    return player1.size();
}

int main(int argc, char *argv[])
{
    deque<int> player1;
    deque<int> player2;
    read_file(player1, player2);

    cout << "Part 1: " << part1(player1, player2) << endl; // 32824

    player1.clear();
    player2.clear();
    read_file(player1, player2);

    cout << "Part 2: "; // 32784 is too low
    if (player1Wins(player1, player2))
        cout << get_score(player1) << endl;
    else
        cout << get_score(player2) << endl;

    return 0;
}
