student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     print(row)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_extract = {row.letter:row.code for (index, row) in data.iterrows()}
# print(data_extract)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = (input("enter the word:  ")).upper()
code_words = [data_extract[code] for code in user_input]
print(code_words)

# for i in user_input:
#     print(data_extract[i])
# code_words = [code.code for code in user_input if user_input in data_extract]

