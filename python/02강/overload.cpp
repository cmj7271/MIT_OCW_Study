#include <iostream>

using namespace std;

int add(int i1, int i2) {
    return i1 + i2;
}

float add(float f1, int i1) {
    return f1 + (float) i1;
}

float add(int i1, float f1) {
    return (float) i1 + f1; 
}



int main(void) {
    int i1 = 1, i2 = 2;
    float f1 = 1.1;

    cout << add(i1, i2) << endl;
    cout << add(i1, f1) << endl;
    cout << add(f1, i2) << endl;
    cout << add(1, 2.2f) << endl;
    
    return 0;
}