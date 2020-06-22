class Solution:
    def replaceSpace(self, s: str) -> str:
    	new = s.split("")
    	temp = ""
    	for i in range(len(temp)):
    		# temp += new[i]+"%20"
    		temp = new[i]+"%20"
    	return str(temp)

if __name__ == '__main__':
	s = "We are happy."
	so=Solution()
	print(so.replaceSpace(s))