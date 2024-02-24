from functools import total_ordering


@total_ordering
class RomanNumeral:
    ROMAN_DICT = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
                  'CM': 900, 'M': 1000}

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __int__(self):
        decimal = 0
        last_value = 0
        for digit in self.number[::-1]:
            value = self.ROMAN_DICT[digit]
            if value >= last_value:
                decimal += value
            else:
                decimal -= value
            last_value = value
        return decimal

    def __add__(self, other):
        return RomanNumeral(RomanNumeral.decimal_to_roman(int(self) + int(other)))

    def __sub__(self, other):
        return RomanNumeral(RomanNumeral.decimal_to_roman(int(self) - int(other)))

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.number == other.number
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) < int(other)
        return NotImplemented

    @staticmethod
    def decimal_to_roman(number):
        roman = ""
        for digit, value in sorted(RomanNumeral.ROMAN_DICT.items(), key=lambda x: -x[1]):
            while number >= value:
                number -= value
                roman += digit
        return roman