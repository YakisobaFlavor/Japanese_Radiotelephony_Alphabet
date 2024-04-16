from jaconv import * # Alphabet↔Hiragana-Katakana Letter Converter
import pandas

# Read Japanese Phonetic Alphabet (和文通話表) from csv file
df = pandas.read_csv("japanese_radiophonetic_alphabet.csv")
dict_phonetic = {df.letter[index]:df.code[index] for (index, row) in df.iterrows()}

numbers_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+']

def enter_input():
    # Input word in Hiragana or Katakana
    input_word = input("Enter a word:")

    # Eval Input
    try:
        for i in input_word:
            if i in numbers_symbols:
                raise ValueError(f"You entered {input_word}, which not contain alphabet, hiragana, or katakana' character")       
        list_code = [dict_phonetic[n] for n in alphabet2kata(input_word) if n in dict_phonetic]
    except KeyError:
        print("Please enter letters in hiragana, katakana, or alphabet only")
        enter_input()
    else:
        print(list_code)

enter_input()
