class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = len(nums) // 3
        c1 = c2 = None
        count1 = count2 = 0

        # getting the candidates
        for num in nums:
            if c1 is not None and num == c1:
                count1 += 1
            elif c2 is not None and num == c2:
                count2 += 1
            elif count1 == 0:
                c1 = num
                count1 = 1
            elif count2 == 0:
                c2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        # verifying the count
        count1 = count2 = 0
        for num in nums:
            if num == c1:
                count1 += 1
            elif num == c2:
                count2 += 1

        majority = []
        if count1 > count:
            majority.append(c1)
        if count2 > count:
            majority.append(c2)
        
        return majority        