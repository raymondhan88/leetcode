class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        string str = to_string(n);
        int l = str.size();
        int i = 0;
        while (i < l - 1 && str[i] <= str[i + 1]) {
            i++;
        }
        if (i < l - 1) {
            while (i > 0 && str[i] - 1 < str[i - 1]) i--;
            str[i]--;
            for (int j = i + 1; j < l; j++) str[j] = '9';
        }
        return stoi(str);
    }
};