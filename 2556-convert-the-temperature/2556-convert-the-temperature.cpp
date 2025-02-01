class Solution {
public:
    const vector<double> convertTemperature(const double celsius) {
        vector<double>result;
        result.push_back(celsius + double(273.15));
        result.push_back((celsius * double(1.80)) + double(32.00));
        return result;
    }
};