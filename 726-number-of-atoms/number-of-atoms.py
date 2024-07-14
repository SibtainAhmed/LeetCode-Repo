class Solution:
    @staticmethod
    def makeStack(formula:str):
        stack = []
        i = 0
        while i<=len(formula)-1:
            curr = formula[i]
            if curr == ')' or curr == '(':
                stack.append(curr)
                i+=1
            elif ord(curr)>=65 and ord(curr)<=90:
                if i+1<len(formula) and (ord(formula[i+1])>=97 and ord(formula[i+1])<=122):
                    stack.append(formula[i:i+2])
                    i+=2
                else:
                    stack.append(curr)
                    i+=1
            else:
                j = 0
                while i+j<len(formula) and ord(formula[i+j])>=48 and ord(formula[i+j])<=57:
                    j+=1
                stack.append(int(formula[i:i+j]))
                i += j
        return stack

    def countOfAtoms(self, formula: str) -> str:
        elementDict = defaultdict(int)
        stack = Solution.makeStack(formula)
        # print(stack)
        mulList = [1]
        currMul = lastMul = lastCummMult = 1
        n = len(stack)
        for _ in range(n):
            # print('currMul = ', currMul)
            val = stack.pop()
            if type(val) == int:
                currMul *= val
                lastMul = val
                continue
            elif val == ')':
                # print('currMul =',currMul, 'lastCummMult = ', lastCummMult)
                mulList.append(currMul//lastCummMult if currMul//lastCummMult else 1)
                lastCummMult = currMul
            elif val == '(':
                rem = mulList.pop()
                currMul = currMul//rem
                lastCummMult = currMul
            else:
                # allElements.add(val)
                # print(val, '+=', currMul)
                # print('mulList = ', mulList)
                elementDict[val] += currMul
                currMul = currMul // lastMul
            lastMul = 1
        allElements = [v for v in elementDict.keys()]
        allElements.sort()
        res = ''
        for val in allElements:
            if elementDict[val] > 1:
                res += val + str(elementDict[val])
            else:
                res += val
        return res              
            