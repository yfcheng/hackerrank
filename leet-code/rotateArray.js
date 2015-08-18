/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var reverse = function(nums, st, end){
    while(st < end){
        var tmp = nums[st];
        nums[st] = nums[end];
        nums[end] = tmp;
        st += 1;
        end -= 1;
    }
};
var rotate = function(nums, k) {
    if( k > nums.length){
        k = k - nums.length;
    }
    if(nums.length > 1 ){
        reverse(nums, 0, nums.length - 1);
        reverse(nums, k, nums.length - 1);
        reverse(nums, 0, k - 1);
    }
};
