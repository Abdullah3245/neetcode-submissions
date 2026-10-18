class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        file = ""
        # traverse through the file and extract the names
        while i < len(path):
            # we encouter '/', so just skip all the consecutive occurance
            if path[i] == '/':
                # end of a filename
                if file and file != ".": 
                    stack.append(file)
                file = ""
                while i < len(path) and path[i] == '/':
                    i += 1
            else: # traversing a name
                file += path[i]
                i += 1
                
        # if ended at a filename, append that as well
        if file and not file.startswith('/') and not file == ".":
            stack.append(file)
        
        # resolve the path
        res = []
        for i in range(len(stack)):
            if stack[i] == "..":
                if res:
                    res.pop()
            else:
                res.append(stack[i])
        return "/" + "/".join(res) if res else "/"
            

            
