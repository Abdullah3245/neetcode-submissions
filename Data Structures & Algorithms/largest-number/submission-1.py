from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare_items(item1, item2):
            if int(item1 + item2) > int(item2 + item1):
                return -1
            return 1
        strings = [str(num) for num in nums]
        strings.sort(key=cmp_to_key(compare_items))

        
        return str(int("".join(strings)))