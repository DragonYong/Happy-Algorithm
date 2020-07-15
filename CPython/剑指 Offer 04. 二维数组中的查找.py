class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
    	i, j = len(matrix), 0
    	while  i > 0 && j < len(matrix[0]):
    		if matrix[i][j] < target: j+=1
    		elif matrix[i][j] > target : i-=1
    		else return True
    	return False


