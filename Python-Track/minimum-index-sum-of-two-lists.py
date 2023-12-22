class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict={}
        for i in range(len(list2)):
            if(list2[i] in list1):
                dict[list2[i]]=i+list1.index(list2[i])
        ans=min(list(dict.values()))
        result=[]
        for i in dict:
            if(dict[i]==ans):
                result.append(i)
        return result
                