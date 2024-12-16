class Solution(object):
    def romanToInt(self, s):
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum = 0
        for i in range(len(s)):
            if i + 1 < len(s) and numerals[s[i]] < numerals[s[i+1]]:
                sum -= numerals[s[i]]  # Subtract the value for this numeral
            else:
                sum += numerals[s[i]]  # Add the value for this numeral
        return sum