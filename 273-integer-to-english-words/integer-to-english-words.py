class Solution:
    def numberToWords(self, num: int) -> str:
        units = ['Thousand', 'Million', 'Billion', 'Trillion']
        unit_digits = {10: 'Ten', 0:'', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        teen_numbers = { 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        tens = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        hundreds = {100: 'One Hundred', 200: 'Two Hundred', 300: 'Three Hundred', 400: 'Four Hundred', 500: 'Five Hundred', 600: 'Six Hundred', 700: 'Seven Hundred', 800: 'Eight Hundred', 900: 'Nine Hundred'}

        def convert(noStr:str):
            res = ''
            if not(noStr): return ''
            no = int(noStr)
            if no < 100:
                if no <= 10:
                    res = ' ' + unit_digits[no]
                elif no > 10 and no<20:
                    res = ' ' +  teen_numbers[no]
                else:
                    res =res +  ' ' + tens[no - no%10]
                    if unit_digits[no%10]:
                        res = res + ' ' + unit_digits[no%10]
            else:
                res = ' ' + hundreds[no - no%100]
                no = no%100
                if no <= 10:
                    res = res + ' ' + unit_digits[no]
                elif no > 10 and no<20:
                    res = res + ' ' +  teen_numbers[no]
                else:
                    res =res +  ' ' + tens[no - no%10]
                    if unit_digits[no%10]:
                        res = res + ' ' + unit_digits[no%10]
            return res

        numStr = str(num)
        finalRes = ''
        temp = ''
        
        temp = convert(numStr[-3:]).strip()
        finalRes =' ' + temp 
        for i in range(1,math.ceil(len(numStr)/3)):
            temp = ''
            st, end = -((i+1)*3), -(i*3)
            temp = convert(numStr[st:end]).strip()
            # print(temp, bool(temp))
            if temp :
                finalRes = ' ' + units[i-1] + ' ' + finalRes.strip()
            finalRes = temp + finalRes
        return finalRes.strip() if finalRes.strip() else 'Zero'