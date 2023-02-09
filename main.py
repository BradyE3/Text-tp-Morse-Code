import pandas

data = pandas.read_csv("alph-to-morse.csv")
morse_dict = {row.letter: row.morse for (index, row) in data.iterrows()}

user_input = input("What would you like translated to morse code: ").upper()


def aplh_to_morse(user_txt):
    coded_msg = ''
    try:
        for letter in user_txt:
            if letter == ' ':
                coded_msg += '/'
            else:
                coded_msg += morse_dict[letter] + ' '

    except KeyError:
        print("Sorry only letters or numbers")

    else:
        print(coded_msg)


aplh_to_morse(user_input)