/*
    Advent of Code Day 25

    To run on a mac:

        1. Update makefile "DAY" variable to 25
        2. Run "make"
        3. Run "./aoc"

    Problem:

        https://adventofcode.com/2020/day/25
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>

using namespace std;

#define INPUT_FILE "input25.txt"
#define TRANSFORM 20201227

long get_loop_size(long key)
{
    long subject_num = 7;
    long value = 1;
    long loop_size = 0;
    while (value != key)
    {
        value = (value * subject_num) % TRANSFORM;
        loop_size++;
    }
    return loop_size;
}

long transform(long loop_size, long subject_num)
{
    long value = 1;
    for (long i = 0; i < loop_size; i++)
        value = (value * subject_num) % TRANSFORM;
    return value;
}

int main(int argc, char *argv[])
{
    // input: the two public keys
    const long card_public_key = 8421034;
    const long door_public_key = 15993936;

    long card_loop_size = get_loop_size(card_public_key);
    cout << card_loop_size << endl;
    long door_loop_size = get_loop_size(door_public_key);
    cout << door_loop_size << endl;

    long card_encryption_key = transform(door_loop_size, card_public_key);
    long door_encryption_key = transform(card_loop_size, door_public_key);

    cout << "Part 1: " << card_encryption_key << " " << door_encryption_key << endl;

    return 0;
}
