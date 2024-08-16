# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            left=0
            right=len(image[i])-1
            while right>left:
                image[i][left],image[i][right]=image[i][right],image[i][left]
                right-=1
                left+=1
            for j in range(len(image[0])):
                image[i][j]=1-image[i][j]
        return image
                