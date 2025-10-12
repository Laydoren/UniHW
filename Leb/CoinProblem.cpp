// CoinProblem.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
using namespace std;

int main() {
    cout << "You have 12 coins. One of them is fake.\n";
    cout << "We will weigh coins and you will tell the position of bowl (e - equal, l - left is lower, r - right is lower).\n";

    string res;

    // 3 группы по 4 монетки
    cout << "\nWeighing 1: coins 1 2 3 4 (l) vs 5 6 7 8 (r)\n";
    cout << "Position of bowl (e, l or r): ";
    cin >> res;

    if (res == "e") { // Среди 9-12 есть фальш
        cout << "\nWeighing 2: coins 9 10 11 (l) vs 1 2 3 (r)\n";
        cout << "Position of bowl (e, l or r): ";
        cin >> res;

        string res1 = res;

        if (res == "e") { // Монета 12 фальш
            cout << "\nWeighing 3: coins 12 (l) vs 1 (r)\n";
            cout << "Position of bowl (l or r): ";
            cin >> res;
            if (res == "l") cout << "\nCoin 12 is fake and it's heavy";
            else if (res == "r") cout << "\nCoin 12 is fake and it's light";
        }

        else { // Среди 9-11 есть фальш
            cout << "\nWeighing 3: coins 9 (l) vs 10 (r)\n";
            cout << "Position of bowl (e, l or r): ";
            cin >> res;
            if (res == "e") { // Монета 11 фальш
                if (res1 == "l") cout << "\nCoin 11 is fake and it's heavy";
                else if (res1 == "r")  cout << "\nCoin 11 is fake and it's light";
            }

            else if (res == "l") { // Монета 9 или 10 фальш
                if (res1 == "l") cout << "\nCoin 9 is fake and it's heavy";
                else if (res1 == "r")  cout << "\nCoin 10 is fake and it's light";
            }

            else if (res == "r") { // Монета 9 или 10 фальш
                if (res1 == "l") cout << "\nCoin 10 is fake and it's heavy";
                else if (res1 == "r")  cout << "\nCoin 9 is fake and it's light";
            }
        }
    }

    else { // фальш 1-8

        string res1 = res;

        cout << "\nWeighing 2: coins 1 2 7 8 (l) vs 3 4 11 12 (r)\n";
        cout << "Position of bowl (e, l or r): ";
        cin >> res;


        // комбинации 1 и 2 взвешиваний
        if ((res1 == "l" && res == "l") || (res1 == "r" && res == "r")) {
            // фальш 1 или 2
            cout << "\nWeighing 3: coin 1 (l) vs coin 2 (r)\n";
            cout << "Position of bowl (l or r): ";
            cin >> res;
            if (res == "l") {
                if (res1 == "l") cout << "\nCoin 1 is fake and it's heavy";
                else cout << "\nCoin 2 is fake and it's light";
            }
            else if (res == "r") {
                if (res1 == "l") cout << "\nCoin 2 is fake and it's heavy";
                else cout << "\nCoin 1 is fake and it's light";
            }
        }

        else if ((res1 == "l" && res == "e") || (res1 == "r" && res == "e")) {
            // фальш 5 или 6
            cout << "\nWeighing 3: coin 5 (l) vs coin 6 (r)\n";
            cout << "Position of bowl (l or r): ";
            cin >> res;
            if (res == "l") {
                if (res1 == "l") cout << "\nCoin 6 is fake and it's light";
                else cout << "\nCoin 5 is fake and it's heavy";
            }
            else if (res == "r") {
                if (res1 == "l") cout << "\nCoin 5 is fake and it's light";
                else cout << "\nCoin 6 is fake and it's heavy";
            }
        }

        else if ((res1 == "l" && res == "r") || (res1 == "r" && res == "l")) {
            // фальш 3, 4, 7, 8
            cout << "\nWeighing 3: coins 3 4 7 (l) vs 9 10 11 (r)\n";
            cout << "Position of bowl (e, l or r): ";
            cin >> res;

            if (res == "e") { // фальш 8
                if (res1 == "l") cout << "\nCoin 8 is fake and it's light";
                else if (res1 == "r")  cout << "\nCoin 8 is fake and it's heavy";
            }

            else { // фальш 3, 4, 7 
                cout << "\nWeighing 4: coin 3 (l) vs coin 4 (r)\n";
                cout << "Position of bowl (e, l or r): ";
                cin >> res;
                if (res == "e") { // фальш 7
                    if (res1 == "l") cout << "\nCoin 7 is fake and it's light";
                    else if (res1 == "r")  cout << "\nCoin 7 is fake and it's heavy";
                }
                else if (res == "l") {
                    if (res1 == "l") cout << "\nCoin 3 is fake and it's heavy";
                    else cout << "\nCoin 4 is fake and it's light";
                }
                else if (res == "r") {
                    if (res1 == "l") cout << "\nCoin 4 is fake and it's heavy";
                    else cout << "\nCoin 3 is fake and it's light";
                }
            }
        }
    }





    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
