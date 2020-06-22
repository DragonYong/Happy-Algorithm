class Solution:
    def findRepeatNumber(self, nums):
    	res_dict = {}
    	for item in nums:
    		if item  in res_dict:
    			return item
    		else:
    			res_dict[item]+=1
   
    			

if __name__ == '__main__':
	input = [1,2,3,4,1,2,3]
	solution = Solution()
	result = solution.findRepeatNumber(input)
	print(result)
