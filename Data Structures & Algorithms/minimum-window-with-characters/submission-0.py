class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        def window_contains(window_map, t_map):
            for key in t_map.keys():
                if t_map[key] > window_map[key]:
                    return False
            return True
        t_map = {}
        window_map = {}

        for c in t:
            if c not in t_map.keys():
                t_map[c] = 1
                window_map[c] = 0
            else:
                t_map[c] = t_map[c] + 1

        unique = len(t_map.keys())

        min_window = ""
        l, r = 0, 0

        while r < len(s):
            if s[r] in window_map.keys():
                window_map[s[r]] += 1
            r += 1
            while window_contains(window_map, t_map):
                print(f"entering at {r}")
                if min_window == "":
                    min_window = s[l:r]
                else:
                    min_window = min(min_window, s[l:r], key=len)
                if s[l] in window_map.keys():
                    print(f"removing {s[l]} at {r}")
                    window_map[s[l]] -= 1
                l += 1

        return min_window
        