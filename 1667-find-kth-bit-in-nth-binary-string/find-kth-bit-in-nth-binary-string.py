class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def makeStr(st):
            temp = []
            for i in reversed(st):
                if i=='1':
                    temp.append('0')
                else:
                    temp.append('1')
            st.append('1')
            st.extend(temp)

        s=['0']
        for _ in range(1,n):
            makeStr(s)
            if len(s)>=k:
                break
        return s[k-1]