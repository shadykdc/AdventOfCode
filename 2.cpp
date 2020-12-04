/*
    Advent of Code Day 2

    To run on a mac:

        1. Update makefile "DAY" variable to 2
        2. Run "make"
        3. Run "./aoc"

    Part 1

    Your flight departs in a few days from the coastal airport; the easiest
    way down to the coast from here is via toboggan.

    The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
    "Something's wrong with our computers; we can't log in!" You ask if you
    can take a look.

    Their password database seems to be a little corrupted: some of the
    passwords wouldn't have been allowed by the Official Toboggan Corporate
    Policy that was in effect when they were chosen.

    To try to debug the problem, they have created a list (your puzzle input)
    of passwords (according to the corrupted database) and the corporate
    policy when that password was set.

    For example, suppose you have the following list:

    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
    Each line gives the password policy and then the password. The password
    policy indicates the lowest and highest number of times a given letter
    must appear for the password to be valid. For example, 1-3 a means that
    the password must contain a at least 1 time and at most 3 times.

    In the above example, 2 passwords are valid. The middle password, cdefg,
    is not; it contains no instances of b, but needs at least 1. The first
    and third passwords are valid: they contain one a or nine c, both within
    the limits of their respective policies.

    How many passwords are valid according to their policies?

    Part 2

    While it appears you validated the passwords correctly, they don't seem to
    be what the Official Toboggan Corporate Authentication System is expecting.

    The shopkeeper suddenly realizes that he just accidentally explained the
    password policy rules from his old job at the sled rental place down the
    street! The Official Toboggan Corporate Policy actually works a little
    differently.

    Each policy actually describes two positions in the password, where 1 means
    the first character, 2 means the second character, and so on. (Be careful;
    Toboggan Corporate Policies have no concept of "index zero"!) Exactly one
    of these positions must contain the given letter. Other occurrences of the
    letter are irrelevant for the purposes of policy enforcement.

    Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
    How many passwords are valid according to the new interpretation of the
    policies?

*/


#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define INPUT_FILE "input2.txt"
#define VAR_COUNT 4
#define MAX_PW_LEN 256

bool password_is_valid_1(
    const int n1, const int n2, const char ch, const char str[MAX_PW_LEN])
{
    int count = 0;
    for (int i = 0; i < strlen(str); i++)
    {
        if (str[i] == ch)
            count++;
        if (count > n2)
            return false;
    }
    if (count < n1)
        return false;

    return true;
}

bool password_is_valid_2(
    const int n1, const int n2, const char ch, const char str[MAX_PW_LEN])
{
    // if both are equal
    if (str[n1-1] == ch && str[n2-1] == ch)
        return false;
    // if one is equal
    else if (str[n1-1] == ch || str[n2-1] == ch)
        return true;
    // none are equal
    return false;
}

int main(int argc, char *argv[])
{
    FILE* pfile;
    int num1;
    int num2;
    char ch;
    char str[MAX_PW_LEN];
    int count1 = 0;
    int count2 = 0;

    pfile = fopen(INPUT_FILE, "r");
    if (pfile == NULL)
    {
        cerr << "Invalid file" << endl;
        exit(1);
    }

    // read file of passwords and check each password
    while(fscanf(pfile, "%d-%d %c: %s", &num1, &num2, &ch, str) == VAR_COUNT)
    {
        if (password_is_valid_1(num1, num2, ch, str))
            count1++;
        if (password_is_valid_2(num1, num2, ch, str))
            count2++;
    }
    fclose(pfile);

    cout << "Part 1: " << count1 << endl; // 607
    cout << "Part 2: " << count2 << endl; // 321

    return 0;
}
