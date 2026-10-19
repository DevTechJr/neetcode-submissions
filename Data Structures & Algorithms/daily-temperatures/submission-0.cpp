class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> temps;
        int temps_len = temperatures.size();
        vector<int> results(temps_len, 0);

        for(int ind = 0; ind < temps_len; ind++){
            while(!temps.empty() && temperatures[ind] > temperatures[temps.top()]){
                int temp_ind = temps.top();
                temps.pop();

                int days = ind - temp_ind;
                results[temp_ind] = days;
            }

            temps.push(ind);
        }

        return results;

    }
};
