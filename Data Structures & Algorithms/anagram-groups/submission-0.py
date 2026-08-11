class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = []
        anagram_dictionary = {}
        for str in strs:
            curr_str = ''.join(sorted(str))
            if curr_str not in anagram_dictionary:
                n = len(anagram)
                anagram_dictionary[curr_str] = n
                anagram.append([str])
            else:
                index = anagram_dictionary[curr_str]
                anagram[index].append(str)
        return anagram