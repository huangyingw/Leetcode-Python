class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return 'Zero'
        divisor = [1000000000, 1000000, 1000, 100, 1]
        self.thousands = ['Billion', 'Million', 'Thousand', 'Hundred', '']
        self.tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.units = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        self.elevens = ['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                        'Nineteen']
        result = ""
        for i in range(len(divisor)):
            if num / divisor[i] == 0:
                continue
            result += self.get_english_word(num / divisor[i]) + " " + self.thousands[i] + ' '
            num = num % divisor[i]
        return result.strip()

    def get_english_word(self, num):
        if num < 10:
            return self.units[num]
        elif num > 10 and num < 20:
            return self.elevens[num % 10]
        elif num < 100:
            return (self.tens[num / 10] + ' ' + self.get_english_word(num % 10)).strip()
        else:
            return (self.units[num / 100] + ' Hundred ' + self.get_english_word(num % 100)).strip()