#include <iostream>
using namespace std;

int main() {
    int p;
    do {
        cout << "Enter base of p (2-36): ";
        cin >> p;
    } while (p < 2 || p > 36);

    char x[50];
    cout << "Enter number: ";
    cin >> x;

    int n[200];
    int len = 1;
    n[0] = 0;


    for (int i = 0; x[i] != '\0'; i++) {
        int d;
        if (x[i] >= '0' && x[i] <= '9')
            d = x[i] - '0';
        else if (x[i] >= 'A' && x[i] <= 'Z')
            d = 10 + x[i] - 'A';
        else if (x[i] >= 'a' && x[i] <= 'z')
            d = 10 + x[i] - 'a';
        else {
            cout << "Wrong symbol: " << x[i] << endl;
            return 0;
        }

        if (d >= p) {
            cout << "Digit " << x[i] << " is not valid for base " << p << endl;
            return 0;
        }


        int carry = 0;
        for (int j = 0; j < len; j++) {
            int t = n[j] * p + carry;
            n[j] = t % 10;
            carry = t / 10;
        }
        while (carry > 0) {
            n[len] = carry % 10;
            carry /= 10;
            len++;
        }


        carry = d;
        int j = 0;
        while (j < len && carry > 0) {
            int t = n[j] + carry;
            n[j] = t % 10;
            carry = t / 10;
            j++;
        }
        while (carry > 0) {
            n[len] = carry % 10;
            carry /= 10;
            len++;
        }
    }

    cout << "Number in decimal base: ";
    for (int i = len - 1; i >= 0; i--) cout << n[i];
    cout << endl;

    return 0;
}
