class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque()

        closest = abs(arr[0] - x)
        index = 0

        for i, num in enumerate(arr):
            diff = abs(x - num)
            if diff < closest:
                index = i
                closest = diff
        
        res.append(arr[index])
        l, r = index - 1, index + 1
        while len(res) < k:
            if l >= 0 and r < len(arr):
                if abs(arr[l] - x) < abs(arr[r] - x):
                    res.appendleft(arr[l])
                    l -= 1
                elif abs(arr[l] - x) == abs(arr[r] - x):
                    res.appendleft(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l >=0:
                res.appendleft(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1

        return list(res)



