class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left,right=0,len(letters)-1
        check=False
        while left<=right:
            mid=left+(right-left)//2
            if letters[mid]>target:
                right=mid-1
            elif letters[mid]<target:
                left=mid+1
            else:
                check=True
                break
        bisect=bisect_right(letters,target)
        if check:
            if bisect==len(letters):
                return letters[0]
            return letters[bisect]
        elif bisect==len(letters):
            return letters[0]
        return letters[bisect_right(letters,target)]