# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)
# print(nato_data.to_dict())

# for (index, row) in nato_data.iterrows():
#     print(row.letter + ":" + row.code)

new_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}
print(new_dict)


def generate_phonetic():
    # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    word = input("Please enter a word: ").upper()
    try:
        nato_list = [new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please!")
        generate_phonetic()
    else:
        print(nato_list)


generate_phonetic()
