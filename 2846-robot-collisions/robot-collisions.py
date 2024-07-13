class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # noOfR = 0
        # for di in directions:
        #     if di == 'R': noOfR +=1
        # if noOfR == len(directions) or not(noOfR):
        #     return directions
        stack = []
        allRobots = [[i,positions[i], healths[i], directions[i]] for i in range(len(healths))]
        allRobots.sort( key= lambda x:x[1])
        print(allRobots)
        for i,p,h,d in allRobots:
            if d == 'R':
                stack.append([p,h,d,i])
                continue
            addRobot = True
            while stack and stack[-1][2] != d:
                if stack[-1][1] == h:
                    stack.pop()
                    addRobot = False
                    break
                elif stack[-1][1] > h:
                    stack[-1][1] -= 1
                    addRobot = False
                    break
                else:
                    ex = stack.pop()
                    # print(ex)
                    h -= 1
            if addRobot:
                stack.append([p,h,d,i])
        # print('stack', stack)
        stack.sort(key=lambda x:x[-1])
        return [val[1] for val in stack]