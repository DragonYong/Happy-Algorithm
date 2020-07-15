class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
    	unordered_map<int, int> m;
    	for (int i = 0; i < unms.size(); ++i)
    	{
    		if(++m[nums[i]] > 1) return nums[i];
    	}
    return 0;
    }
};