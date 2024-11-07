/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map1 = new Map();
    for(let i=0; i<nums.length; i++){
        let val = nums[i];
        if (map1.has(target-val)){
            return [map1.get(target-val), i]
        }
        map1.set(val, i);
    }
    return [0,1]
};