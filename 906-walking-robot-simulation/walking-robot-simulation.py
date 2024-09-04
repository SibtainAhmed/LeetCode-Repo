class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # obs = set(obstacles)
        obs = {str(ob) for ob in obstacles}
        maxD = 0
        curr = [0,0]
        ds = ['N', 'E', 'S', 'W']
        d = 0
        for c in commands:
            if c < 0:
                if c == -1:
                    d = (d+1) % 4
                else:
                    d = (d-1+4) % 4
                    # print(d)
            else:
                if d == 0:
                    for _ in range(c):
                        curr[1] += 1
                        if str(curr) in obs:
                            curr[1] -= 1
                            break
                elif d == 1:
                    for _ in range(c):
                        curr[0] += 1
                        if str(curr) in obs:
                            curr[0] -= 1
                            break
                elif d == 2:
                    for _ in range(c):
                        curr[1] -= 1
                        if str(curr) in obs:
                            curr[1] += 1
                            break
                else:
                    for _ in range(c):
                        curr[0] -= 1
                        if str(curr) in obs:
                            curr[0] += 1
                            break
                # print(curr)
                val = curr[0]**2 + curr[1]**2
                maxD = max(maxD, val)
        return maxD