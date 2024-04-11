from jcconv3 import * # Japanese Hiragana-Katakana Letter Converter
import pandas

# Read Japanese Phonetic Alphabet (和文通話表) from csv file
df = pandas.read_csv("japanese_radiophonetic_alphabet.csv")
dict_phonetic = {df.letter[index]:df.code[index] for (index, row) in df.iterrows()}

# Input word in Hiragana or Katakana
input_word = input("Enter a word:")

# Split the letter and print the phonetic spelling
list_code = [dict_phonetic[n] for n in hira2kata(input_word) if n in dict_phonetic]
print(list_code)