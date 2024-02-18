class Solution:
    def simplifyPath(self, path: str) -> str:
        path_name, stack = path.split('/') , []
        for name in path_name:
            if name==".." and stack:
                stack.pop()
            elif name!="." and name!="" and name!="..":
                stack.append(name)
        return "/"+"/".join(stack)