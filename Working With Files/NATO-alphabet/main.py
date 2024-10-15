import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_extract = {row.letter:row.code for (index, row) in data.iterrows()}
# print(data_extract)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

check = True

while check:
    user_input = (input("enter the word:  ")).upper()
    try:
        code_words = [data_extract[code] for code in user_input]
    except KeyError:
        print("sorry, only letters in the alphabet please")
    else:
        print(code_words)
        check = False

# for i in user_input:
#     print(data_extract[i])
# code_words = [code.code for code in user_input if user_input in data_extract]

