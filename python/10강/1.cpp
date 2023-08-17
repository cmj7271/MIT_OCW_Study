#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(vector<int> arr, int depth, int result);

int main() {
    int length = 0;
    cin >> length;
    vector<int> arr(length);
    for(int i = 0; i < length; i++) cin >> arr[i];

    int result = -800;
    result = solve(arr, 0, result);

    cout << result;

    return 0;
}

int solve(vector<int> arr, int depth, int result) {
    if(depth == arr.size()) {
        int tmp = 0;
        for(int i = 0; i < arr.size() - 1; i++) {
            tmp += abs(arr[i] - arr[i + 1]);
        }
//        for(int n : arr) cout << n << " ";
//        cout << '\n';

        if(result < tmp) result = tmp;
        return result;
    }

    for(int i = depth; i < arr.size(); i++) {
        swap(arr[i], arr[depth]);
        result = solve(arr, depth + 1, result);
        swap(arr[depth], arr[i]);
    }

    return result;
}