#Exercise 1

# Create a list of capital letters in the english alphabet
capitalLetters = [chr(i) for i in range(65,91)]

#Create a list of capital letter from the english alphabet, 
#but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
exclWords = [chr(i) for i in range(65,91) if i not in [70, 75, 80, 85]]
print(exclWords)

#Create a list of capital letter from from the english alphabet, 
#but exclude every second letter between F & O
exclSecond = [chr(i) for i in range(65,91) if i not in range(70, 80, 2)]
print(exclSecond)


#Exercise 2

#From 2 lists, using a list comprehension, create a list containing:
#[(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), 
#(‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]
colorList = ["Black", "White"]
sizeList = ["s", "m", "l", "xl"]

tupleList = [(c,s) for c in colorList for s in sizeList]
print(tupleList)

#If the tuple pair is in the following list,
#it should not be added to the comprehension generated list: [('Black', 'm'), ('White', 's')]
singled_out = [('Black', 'm'), ('White', 's')]
tupleListExcl = [(c,s) for c in colorList for s in sizeList if (c,s) not in singled_out]
print(tupleListExcl)


