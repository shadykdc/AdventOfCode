/*
    Advent of Code Day 21

    To run on a mac:

        1. Update makefile "DAY" variable to 21
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/21
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <deque>
#include <sstream>
#include <unordered_set>

using namespace std;

#define INPUT_FILE "input21.txt"

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
    string str;
    for (auto num : player1)
        str += to_string(num);
    for (auto num : player2)
        str += to_string(num);
    if (seen.find(str) != seen.end())
        return true;
    seen.insert(str);
    return false;
}

bool player1Wins(deque<int>& player1, deque<int>& player2,
    unordered_set<string>& seen)
{
    if (seen_before(player1, player2, seen)) return true;
    if (player1.size() == 0) return false;
    if (player2.size() == 0) return true;

    cout << "p1: ";
    for (auto num : player1) cout << num << " ";
    cout << endl;
    cout << "p2: ";
    for (auto num : player2) cout << num << " ";
    cout << endl;

    int card1 = player1.front();
    int card2 = player2.front();
    player1.pop_front();
    player2.pop_front();

    if (card1 <= player1.size() && card2 <= player2.size())
    {
        if (player1Wins(player1, player2, seen))
        {
            player1.push_back(card1);
            player1.push_back(card2);
            return true;
        }
        player2.push_back(card2);
        player2.push_back(card1);
        return false;
    }

    if (card1 > card2)
    {
        player1.push_back(card1);
        player1.push_back(card2);
        return true;
    }
    player2.push_back(card2);
    player2.push_back(card1);
    return false;
}

int main(int argc, char *argv[])
{
    deque<int> player1;
    deque<int> player2;
    unordered_set<string> seen;
    read_file(player1, player2);

    cout << "Part 1: " << part1(player1, player2) << endl; // 32824
    cout << "Part 2: ";
    player1.clear();
    player2.clear(); cout << endl;
    read_file(player1, player2);
    if (player1Wins(player1, player2, seen))
        cout << get_score(player1) << endl;
    else
        cout << get_score(player2) << endl;

    return 0;
}
