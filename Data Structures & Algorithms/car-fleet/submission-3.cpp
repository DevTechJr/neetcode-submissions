class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        stack <double> times;
        int length = position.size();

        vector<pair<int,int>> cars;
        for(int i = 0; i < length; i++){
            cars.push_back({position[i], speed[i]});
        }

        sort(cars.begin(), cars.end());

        for(int ind = length -1; ind >= 0; ind--){
            double time = (double)(target - cars[ind].first)/(cars[ind].second);

            if(times.empty() || time > times.top()){
                times.push(time);
            }

        }

        return times.size();
    }
};
