/*Rotate an array to the right by k steps in-place without allocating extra space. For
instance, with k = 3, the array [0, 1, 2, 3, 4, 5, 6] is rotated to [4, 5, 6, 0, 1, 2, 3].
*/

var reverse = function(numbers, st, end){
	var temp = "";
	while(st < end){
		temp = numbers[st];
		numbers[st] = numbers[end];
		numbers[end] = temp;
		st ++;
		end --;
	}
	return numbers;
};

var rotate = function(nums, k){
	nums = reverse(nums, 0, nums.length - 1);
	nums = reverse(nums, 0, k - 1);
	nums = reverse(nums, k, nums.length - 1);
	return nums;
};

console.log( rotate([0,1,2,3,4,5,6], 3) );

console.log( rotate(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 3) );