class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        for (int j=0; j<nums.size(); j++){
            numMap[nums[j]] = j;
        }
        for (int i=0; i < nums.size(); i++){
            int diff = target - nums[i];
                if (numMap.count(diff) && numMap[diff] != i){
                    return {i,numMap[diff]};
                
            }
        }
    return {0,0};
    }
};