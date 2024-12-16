class Solution(object):
    def romanToInt(self, s):
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        roman_array = []
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] == "I" and s[i+1] == "V":
                roman_array.append("IV")
                i += 2
            elif i + 1 < len(s) and s[i] == "I" and s[i+1] == "X":
                roman_array.append("IX")
                i += 2
            elif i + 1 < len(s) and s[i] == "X" and s[i+1] == "L":
                roman_array.append("XL")
                i += 2
            elif i + 1 < len(s) and s[i] == "X" and s[i+1] == "C":
                roman_array.append("XC")
                i += 2
            elif i + 1 < len(s) and s[i] == "C" and s[i+1] == "D":
                roman_array.append("CD")
                i += 2
            elif i + 1 < len(s) and s[i] == "C" and s[i+1] == "M":
                roman_array.append("CM")
                i += 2
            else:
                roman_array.append(s[i])
                i += 1

        roman_sum = 0
        for numeral in roman_array:
            value = roman_numerals.get(numeral)
            roman_sum += value
        return roman_sum
solution = Solution()
result = solution.romanToInt("CMCDIXIV")
print(result)