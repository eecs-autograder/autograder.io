#include <iostream>
#include <string>
using namespace std;

int main() {
    // Intentional bug when input only has one word
    string word;
    cin >> word;
    while (cin) {
        cout << word << endl;
        cin >> word;
    }
}
