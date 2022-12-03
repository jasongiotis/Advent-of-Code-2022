#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;
int main()
{

    ifstream file("input.txt");
    string line;
    int valid = 0;
    vector<int> best_elves;
    int sum = 0;

    while (getline(file, line))
    {

        if (line.empty())
        {

            if (best_elves.size() != 3)
            {
                best_elves.push_back(atoi(line.c_str()));
            }
            else
            {
                sort(best_elves.begin(), best_elves.end());
                if (sum > best_elves[0])
                {
                    best_elves[0] = sum;
                }
            }
            sum = 0;
        }
        else
        {
            sum += atoi(line.c_str());
        }
    }

    cout << "The top 3  elves  are : " << best_elves[0] << ", " << best_elves[1] << ", " << best_elves[2] << endl;
    cout << "The sum of the top 3 elves is : " << best_elves[0] + best_elves[1] + best_elves[2] << endl;
}