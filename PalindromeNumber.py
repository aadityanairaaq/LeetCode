class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        listedX = list(strX)
        for i in range(len(listedX)):
            if listedX[i] != listedX[-i-1]:
                return False
        return True