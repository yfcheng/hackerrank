

var sort = function sort(nums){
	for(var i = 0;i < nums.length;i++){
		for(var j = 0;j < nums.length;j++){
			if(nums[j] > nums[i]){
				var tmp = nums[j];
				nums[j] = nums[i];
				nums[i] = tmp;
			}
		}
	}
	return nums;
};



console.log( sort([2,8,5,1,4,3,7]) );