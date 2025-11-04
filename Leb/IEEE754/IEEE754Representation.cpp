#include <iostream>
using namespace std;

int main() {
    double number;
    cout << "Enter num:";
    cin >> number;

    unsigned long long bits = *(unsigned long long*)&number;

    unsigned long long exponent_bits = (bits >> 52) & 0x7FF;
    unsigned long long mantissa = bits & 0xFFFFFFFFFFFFF;

    int dot_position = exponent_bits - 1023 + 1;

    if (dot_position <= 0) {
        cout << "0.";
        for (int i = 0; i < -dot_position; i++) cout << "0";

        cout << "1";
        for (int i = 51; i >= 0; i--) cout << ((mantissa >> i) & 1);
    }
    else {
        int bit_count = 1;
        cout << "1";

        for (int i = 51; i >= 0; i--) {
            if (bit_count == dot_position) cout << ".";
            cout << ((mantissa >> i) & 1);
            bit_count++;
        }
    }

    cout << endl;
    return 0;
}