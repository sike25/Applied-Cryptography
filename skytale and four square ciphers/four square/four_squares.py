## FILLING THE FOUR SQUARE MATRIX
import nltk
from itertools import combinations, permutations
from nltk.corpus import words

nltk.download('words')
missingLetters = "ablmnortuwxyz"
english_words = set(words.words())
combinations_list = list(combinations(missingLetters, 4))
incompleteWord = "p--h--"
    
print()
print("filling the four square matrices...")
for combo in combinations_list:
    for perm in permutations(combo):
        wordToPrint = "p"+perm[0]+perm[1]+"h"+perm[2]+perm[3]
        if wordToPrint in english_words:
            print(wordToPrint)

missingLetters = "cdfghijmosvwxyz"
incompleteWord = "-pen"
for letter in missingLetters:
    wordToPrint = letter+"pen"
    if wordToPrint in english_words:
        print(wordToPrint)

print()

## DECRYPTION
print("decrypting...")

fourSquareMatrix = [["a", "b", "c", "d", "e", "P", "Y", "T", "H", "O"],
                    ["f", "g", "h", "i", "j", "N", "A", "B", "C", "D"],
                    ["k", "l", "m", "n", "o", "E", "F", "G", "I", "J"],
                    ["p", "r", "s", "t", "u", "K", "L", "M", "R", "S"],
                    ["v", "w", "x", "y", "z", "U", "V", "W", "X", "Z"],
                    ["O", "P", "E", "N", "A", "a", "b", "c", "d", "e"],
                    ["B", "C", "D", "F", "G", "f", "g", "h", "i", "j"],
                    ["H", "I", "J", "K", "L", "k", "l", "m", "n", "o"],
                    ["M", "R", "S", "T", "U", "p", "r", "s", "t", "u"],
                    ["V", "W", "X", "Y", "Z", "v", "w", "x", "y", "z"]]
openMap = { 
    "O":(5,0), "P":(5,1), "E":(5,2), "N":(5,3), "A":(5,4), 
    "B":(6,0), "C":(6,1), "D":(6,2), "F":(6,3), "G":(6,4), 
    "H":(7,0), "I":(7,1), "J":(7,2), "K":(7,3), "L":(7,4), 
    "M":(8,0), "R":(8,1), "S":(8,2), "T":(8,3), "U":(8,4), 
    "V":(9,0), "W":(9,1), "X":(9,2), "Y":(9,3), "Z":(9,4)
    }

pythonMap = {
    "P":(0,5), "Y":(0,6), "T":(0,7), "H":(0,8), "O":(0,9), 
    "N":(1,5), "A":(1,6), "B":(1,7), "C":(1,8), "D":(1,9), 
    "E":(2,5), "F":(2,6), "G":(2,7), "I":(2,8), "J":(2,9), 
    "K":(3,5), "L":(3,6), "M":(3,7), "R":(3,8), "S":(3,9), 
    "U":(4,5), "V":(4,6), "W":(4,7), "X":(4,8), "Z":(4,9)
    }

input = "JKMIYHIWCBJPKESPEUHLHACKSNXSJJON" + "MFHMJEHHRXJUSPHOHHYYRCSNRSRCFFKD" \
        "SIEEINSKMFPGAKYZCDTDYMOAGNIAHACK" + "TMSOHDCBOEGNIACKCCDOGNIACKCCRJIU" \
        "KSTANFDNHTDEONNOLLRFKSEPKFFUIEPU"+ "HLONITSEOLSOFNPMSOINHASKMFTLIAOL" \
        "SOGTMFPGAKHGFNCKYMWKIAHLFZMFHAHM" + "HBLSPAPNINVRCTSNIFITDEDHMIEGHWSN" \
        "SJOCTAMTMFBTJJONMDJUIPOPMUHADHKP" + "FICBJPRSNERNILMNILKNCKSNXS"


# Iterate through the string two characters by two characters
output = ""
for i in range(0, len(input), 2):
    piece = input[i:i+2]
    firstCoord = pythonMap[piece[0]]
    secondCoord = openMap[piece[1]]

    a = fourSquareMatrix[firstCoord[0]][secondCoord[1]]
    b = fourSquareMatrix[secondCoord[0]][firstCoord[1]]

    output = output + a + b
print(output)
print()


