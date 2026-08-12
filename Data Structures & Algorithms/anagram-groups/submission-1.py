class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_index = {}
        index = 0
        anagrams = []

        for s in strs:
            ordered = ''.join(sorted(s))
            if ordered in string_index:
                i = string_index[ordered]
                anagrams[i].append(s)
            else:
                anagrams.append([s])
                string_index[ordered] = index
                index +=1
        
        return anagrams