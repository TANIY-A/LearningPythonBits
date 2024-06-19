# converting a word into number
def word_to_number(word):
    ones={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    teen={"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19}
    tens={"ten":10,"twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90}
    bigdigit={"hundred":100,"thousand":1000,"lakhs":100000,"cores":1000000}

    word_split=word.split()
    current_value=0
    number=0
    for element in word_split:
        if element in ones:
            current_value+=ones[element]
        elif element in teen:
            current_value+=teen[element] 
        elif element in tens:
            current_value+=tens[element]
        elif element in bigdigit:
            current_value*=bigdigit[element]
            number+=current_value
            current_value=0
        elif element == "and":
            continue
    number+=current_value

    return (number)

    

# main function
sample="fifty thousand ninety"
print(word_to_number(sample))
