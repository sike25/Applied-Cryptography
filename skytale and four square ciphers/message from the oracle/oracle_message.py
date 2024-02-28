
cipherText = "Fwa  L oatwnakry aoci eastenydnt dgo deta uS dhef pg amrialbtoonroy nmhtr t  aaiPhmHb oeeueiEurnsrtiss taat it cnhcahmlteineoesrt  us  ymbr oy eonlfomnu i uu nanwrsOd ei tr d dg  oe erbifa  eef d"

# Try various period lengths
for periodLength in range(1, int(len(cipherText)/2)):
    print()
    print("PERIOD LENGTH: ", periodLength)

    columnLength = int(len(cipherText) / periodLength) + 1
    matrix = [[' ' for _ in range(columnLength)] for _ in range(periodLength)] 

    # Fill the matrix with characters from the string
    index = 0
    for row in range(columnLength):
        for col in range(periodLength):
            if index == len(cipherText):
                    break
            matrix[col][row] = cipherText[index]
            index += 1

    # Print the matrix in the desired format
    for row in matrix:
        print(" ".join(row))

