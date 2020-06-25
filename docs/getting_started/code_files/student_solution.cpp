#include <iostream>
#include <string>
using namespace std;

int main() {
    // Intentional bug when input has more than one word
    string word;
    cin >> word;
    cout << word << endl;
    cin >> word;
    while (cin) {
        cin >> word;
        cout << word << endl;
    }
}
