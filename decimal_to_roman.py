class RomanNumerals:

#1977

    dict = {
        '1': "I",
        '4': 'IV',
        '5': 'V',
        '10': 'X',
        '50': 'L',
        '100': 'C',
        '500': 'D',
        '1000': 'M'
    }

    def split_num(self,num):
        split_decimal = []
        num_list = [n for n in num]
        len_num_list = len(num_list) - 1
        for n in num_list:
            t = n+(str(0) * len_num_list)
            len_num_list = len_num_list - 1
            split_decimal.append(t)
        return split_decimal


    def to_roman(self,num):
        roman_num = []
        split_number = self.split_num(num)
        for num in split_number:
            if num == 0:
                continue

        return ','.join(roman_num)

num = RomanNumerals()
print(num.to_roman('1947'))










