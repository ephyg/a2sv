# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

# Masha and a Beautiful Tree
for i in range(int(input())):
    n=int(input())
    nums = [int(i) for i in input().split()]
    answer=0
    flag=True
    def merge_sort(nums,left,right):
        if right==left:
            return [nums[left]]
        
        mid=left+(right-left)//2
        left_side=merge_sort(nums,left,mid)
        right_side=merge_sort(nums,mid+1,right)

        if flag:
            return merge(nums,left_side,right_side)
    def merge(nums,left_side,right_side):
        global answer,flag
        check1=right_side+left_side
        check2=left_side+right_side
        x=sorted(check1)
        if x==check1:
            answer+=1
            return x
        elif check2==x:
            return x
        else:
            flag=False
            answer=-1
            return []
    merge_sort(nums,0,len(nums)-1)
    print(answer)
        



