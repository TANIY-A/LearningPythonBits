def number_to_word(number):
    ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    teens = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens = {10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

    if number == 0:
        return "zero"
    
    if number in ones:
        return ones[number]
    if number in teens:
        return teens[number]
    if number in tens:
        return tens[number]
    
    if number < 100:
        ten_part = (number // 10) * 10
        one_part = number % 10
        if one_part != 0:
            return tens[ten_part] + " " + ones[one_part]
        else:
            return tens[ten_part]
    
    if number < 1000:
        hundred_part = number // 100
        remainder = number % 100
        if remainder == 0:
            return ones[hundred_part] + " hundred"
        else:
            return ones[hundred_part] + " hundred and " + number_to_word(remainder)
    
    if number < 100000:
        thousand_part = number // 1000
        remainder = number % 1000
        if remainder == 0:
            return number_to_word(thousand_part) + " thousand"
        else:
            return number_to_word(thousand_part) + " thousand " + number_to_word(remainder)
    
    if number < 10000000:
        lakh_part = number // 100000
        remainder = number % 100000
        if remainder == 0:
            return number_to_word(lakh_part) + " lakh"
        else:
            return number_to_word(lakh_part) + " lakh " + number_to_word(remainder)
    
    if number <= 99999999:
        crore_part = number // 10000000
        remainder = number % 10000000
        if remainder == 0:
            return number_to_word(crore_part) + " crore"
        else:
            return number_to_word(crore_part) + " crore " + number_to_word(remainder)
# main function
num=13990
print (number_to_word(num) )
        
    