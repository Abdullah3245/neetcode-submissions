class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1

        num_boats = 0

        while l <= r:
            remain = limit - people[r]
            num_boats += 1

            r -= 1

            if l <= r and remain >= people[l]:
                l += 1
        
        return num_boats