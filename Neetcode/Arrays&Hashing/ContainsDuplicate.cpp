#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> map;
        for(unsigned int i=0;i<nums.size();i++){
            if(map.find(nums[i]) != map.end()){
                return true;
            } // {1,2,3,1}
            map[nums[i]] = 1;
        }
        return false;
    }
};

int main() {
    vector<int> nums = {1,2,3,0};
    Solution solution;
    bool result = solution.containsDuplicate(nums);
    cout << result << endl;
    return 0;
}