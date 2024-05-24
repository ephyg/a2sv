# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1


from collections import defaultdict, deque
class Solution:
    def findOrder(self,names, n, K):
    # code here
        graph=defaultdict(list)
        degree=defaultdict(int)
        flag=False
        letters=set()
        for let in names:
            for i in let:
                letters.add(i)
        for i in range(1,n):
            if names[i][0]!=names[i-1][0]:
                graph[names[i-1][0]].append(names[i][0])
                degree[names[i][0]]+=1
            else:
                pointer=0
                while len(names[i])>pointer and len(names[i-1])>pointer:
                    if names[i][pointer]==names[i-1][pointer]:
                        if pointer==len(names[i])-1 and len(names[i]) < len(names[i-1]) :
                            flag=True
                            break
                    else:
                        graph[names[i-1][pointer]].append(names[i][pointer])
                        degree[names[i][pointer]]+=1
                        break
                    pointer+=1
                        
        queue=deque()
        for i in range(ord("a"),ord("z")+1):
            if degree[chr(i)]==0 and chr(i) in letters:
                queue.append(chr(i))
        ans=[]
        
        while queue:
            node=queue.popleft()
            ans.append(node)
            for neighbour in graph[node]:
                degree[neighbour]-=1
                if degree[neighbour]==0:
                    queue.append(neighbour)
        
        if len(ans)!=K and flag:
            return "0"
        else:
            return "".join(ans)
# print(queue)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends